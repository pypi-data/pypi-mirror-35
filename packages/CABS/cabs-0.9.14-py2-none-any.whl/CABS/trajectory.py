import StringIO
import numpy as np
import os
from copy import deepcopy
from CABS import logger
from CABS import align
from CABS import utils
from CABS.atom import Atom, Atoms

__all__ = ['Trajectory', 'Header']
_name = 'Trajectory'


class Header(object):
    """Trajectory header read from CABS output: energies and temperatures"""

    class CannotMerge(Exception):
        """Raised when trying to merge headers for different frames"""

        def __init__(self, h1, h2):
            self.msg = 'Cannot merge headers: %s and %s' % (h1, h2)

        def __str__(self):
            return self.msg

    def __init__(self, line):
        header = line.split()
        self.model = int(header[0])
        self.length = (int(header[1]) - 2,)
        self.energy = np.matrix(header[2: -2], float)
        self.temperature = float(header[-2])
        self.replica = int(header[-1])
        self.rmsd = 0

    def __repr__(self):
        return 'Replica: %d Model: %d Length: %s T: %.2f E: %s' % (
            self.replica,
            self.model,
            self.length,
            self.temperature,
            str(self.energy.tolist())
        )

    def __add__(self, other):
        """Merges two headers from two chains of the same frame"""
        if self.replica != other.replica or self.model != other.model:
            raise Header.CannotMerge(self, other)
        else:
            dt = self.temperature - other.temperature
            if dt ** 2 > 1e-6:
                raise Exception("Cannot merge headers with different T!!!")
            else:
                h = deepcopy(self)
                h.length += other.length
                h.energy = np.concatenate([self.energy, other.energy])
        return h

    def get_energy(self, mode='interaction', number_of_peptides=None):
        """
        Calculates chosen energy for given frame.
        :param mode: string Mode of calculation for further development. Currently supports 'total'
        for total energy and 'interaction' for protein-peptide interactions.
        :param number_of_peptides: int the number of peptides in the model.
        :return: int the energy value.
        """
        if mode == 'interaction':
            # number_of_peptides fixes energy calculations
            if number_of_peptides is None:
                print("Unknown number of peptides. Assuming 1.")
                num_pept = 1
            else:
                num_pept = number_of_peptides
            int_submtrx_size = self.energy.shape[0] - num_pept
            int_enrg = np.sum(self.energy[:int_submtrx_size, -num_pept:])
            return int_enrg
        elif mode == 'total':
            return np.sum(np.tril(self.energy))


class Trajectory(object):
    """
    Class holding compressed trajectory.
    """
    GRID = 0.61

    def __init__(self, template, coordinates, headers, number_of_peptides=None, weights=None):
        self.template = template
        self.coordinates = coordinates
        self.headers = headers
        self.rmsd_native = None
        self.number_of_peptides = number_of_peptides
        self.weights = np.diagflat(weights) if weights else None

    @staticmethod
    def read_seq(filename):
        atoms = []
        with open(filename) as f:
            for i, line in enumerate(f):
                atoms.append(
                    Atom(
                        hetatm=False,
                        serial=i + 1,
                        name='CA',
                        alt=line[7],
                        resname=line[8:11],
                        chid=line[12],
                        resnum=int(line[1:5]),
                        icode=line[5],
                        occ=float(line[15]),
                        bfac=float(line[16:22])
                    )
                )
        return atoms

    @staticmethod
    def read_traf(filename):
        headers = []
        replicas = {}

        def save_header(h):
            headers.append(h)

        def save_coord(c, r):
            if r not in replicas:
                replicas[r] = []
            replicas[r].extend(c[3:-3])

        with open(filename) as f:
            current_header = None
            current_coord = []
            for line in f:
                if '.' in line:
                    header = Header(line)
                    if not current_header:
                        current_header = header
                    else:
                        save_coord(current_coord, current_header.replica)
                        current_coord = []
                        try:
                            current_header = current_header + header
                        except Header.CannotMerge:
                            save_header(current_header)
                            current_header = header
                else:
                    current_coord.extend(map(int, line.split()))
            save_header(current_header)
            save_coord(current_coord, current_header.replica)

        headers.sort(key=lambda x: x.model)
        headers.sort(key=lambda x: x.replica)
        coordinates = np.array([Trajectory.GRID * x for y in sorted(replicas) for x in replicas[y]])

        return headers, coordinates

    @classmethod
    def read_trajectory(cls, traf, seq):
        template = Atoms(Trajectory.read_seq(seq))
        headers, coordinates = Trajectory.read_traf(traf)

        replicas = len(set(h.replica for h in headers))
        if len(headers) % replicas:
            raise Exception('Replicas have different sizes!!!')
        models = len(headers) / replicas
        length = headers[0].length

        if any(length != h.length for h in headers):  # check if all frames have the same shape
            raise Exception('Invalid headers in %s!!!' % traf)

        sum_length = sum(length)

        if sum_length != len(template):
            # check if number of atoms in SEQ matches that in trajectory headers
            raise Exception('Different number of atoms in %s and %s!!!' % (traf, seq))

        # final test if information from headers agrees with number of coordinates
        size_test = replicas * models * sum_length * 3
        if size_test != len(coordinates):
            raise Exception('Invalid number of atoms in %s!!!' % traf)

        coordinates = coordinates.reshape(replicas, models, sum_length, 3)
        return cls(template, coordinates, headers)

    def select(self, selection=None, template=None):
        """
        Arguments:
        selection -- str;
        template -- Atoms instance.

        One of the arguments has to be passed.
        """
        if not template:
            template = self.template.select(selection)
        inds = [self.template.atoms.index(a) for a in template]
        return Trajectory(template, self.coordinates[:, :, inds, :], self.headers)

    def to_atoms(self):
        result = Atoms()
        num = 0
        shape = self.coordinates.shape
        for model in self.coordinates.reshape(-1, len(self.template), 3):
            atoms = deepcopy(self.template)
            num += 1
            atoms.set_model_number(num)
            atoms.from_numpy(model)
            result.extend(atoms)
        self.coordinates.reshape(shape)
        return result

    def rmsd_matrix(self, msg=''):
        """
        Calculates rmsd matrix with no fitting for all pairs od models in trajectory.
        :return: np.array
        """

        models = self.coordinates.reshape(-1, len(self.template), 3)
        dim = len(models)
        result = np.zeros((dim, dim))

        if msg:
            bar = logger.ProgressBar((dim * dim - dim) / 2, start_msg=msg)
        else:
            bar = None
        for i in range(dim):
            for j in range(i + 1, dim):
                if bar:
                    bar.update()
                result[i, j] = result[j, i] = utils.rmsd(models[i], models[j])
        if bar:
            bar.done(True)
        return result

    def superimpose_to(self, reference, substructure=None):
        """Superimposes trajectory substructure from self.template on given reference.

        Arguments:
        reference -- structure template is to be superimposed on.
        substructure -- selection of atoms from self.template aligned with given reference.

        This method modifies trajectory in place.
        """

        if substructure:
            pieces = utils.ranges([self.template.atoms.index(a) for a in substructure])
        else:
            pieces = [(0, len(self.template))]

        target = reference.to_numpy()

        if self.weights:
            t_com = np.average(target, axis=0, weights=self.weights)
            target = target - t_com

            for model in self.coordinates.reshape(-1, len(self.template), 3):
                query = np.concatenate([model[slice(*piece)] for piece in pieces])
                query = query - np.average(query, axis=0, weights=self.weights)
                query = np.dot(query, utils.kabsch(target, query, weights=self.weights, concentric=True)) + t_com
                np.copyto(model, query)

        else:  # dynamic weights
            for model in self.coordinates.reshape(-1, len(self.template), 3):
                query = np.concatenate([model[slice(*piece)] for piece in pieces])
                rmsd, rot, t_com, q_com = utils.dynamic_kabsch(target, query)
                np.copyto(model, np.dot(model - q_com, rot) + t_com)

    def align_to(self, ref_stc, ref_chs, self_chs, align_mth='SW', kwargs={}):
        """Calculates alignment of template to given reference structure.

        Arguments:
        ref_stc -- CABS.PDBlib.PDB instance of reference structure.
        ref_chs -- str; chain id(s) of reference selection.
        self_chs -- str; chain id(s) of trajectory structure selection.
        align_mth -- str; name of aligning method to be used. See CABS.align documentation for more information.
        kwargs -- as above, but used when aligning target protein.

        One needs to specify chains to be taken into account during alignment calculation.

        Returns two structures: reference and template -- both cropped to aligned parts only,
        and alignment as list of tuples.
        """
        return align.align_to(ref_stc, ref_chs, self.template, self_chs, align_mth, kwargs)

    def rmsd_to_reference(self, ref_sstc, self_sstc):
        """Returns list of RMSDs of given substructure of template to given reference.

        Arguments:
        ref_sstc -- CABS.PDBlib.PDB instance of reference structure (only residues aligned with template.
        self_sstc -- self.template substructure aligned with given reference and for which RMSD is to be calculated.

        Both given substructure have to be the same length (and in aligned order).
        """

        ref_trg = np.array(ref_sstc.to_numpy())
        aln_traj = self.select(template=self_sstc)
        models = aln_traj.coordinates.reshape(-1, len(aln_traj.template), 3)
        result = np.zeros(len(models))
        for i, h in zip(range(len(models)), self.headers):
            result[i] = utils.rmsd(models[i], ref_trg)
            h.rmsd = result[i]
        return result

    def get_model(self, model):
        shape = self.coordinates.shape
        coordinates = self.coordinates.reshape(-1, len(self.template), 3)[model]
        atoms = deepcopy(self.template)
        atoms.set_model_number(model + 1)
        m = atoms.from_numpy(coordinates)
        self.coordinates.reshape(shape)
        return m

    def to_pdb(self, name=None, mode='models', to_dir=None):
        """
        Method for transforming a trajectory instance into a PDB file-like object.
        :param name:    'name'  -- name (name) ;)
        :param mode:    'models' -- the method returns a list of StringIO objects,
                                    each representing one model from the trajectory;
                        'replicas' -- the method returns a list of StringIO objects,
                                      each representing one replica from the trajectory.
        :param to_dir:  path to directory in which the PDB files should be saved.
                        If None, only StringIO object is returned.
        :return:        if to_dir is None: StringIO object
                        if to_dir is not None: saves file and returns True.
        """
        execution_mode = {'models': (self.coordinates[0], 'model'), 'replicas': (self.coordinates, 'replica')}
        if to_dir:
            for i, m in enumerate(execution_mode[mode][0]):
                pre = execution_mode[mode][1] if name is None else name
                post = '' if len(execution_mode[mode][0]) == 1 else '_{0}'.format(i)
                fname = os.path.join(to_dir, '%s%s.pdb' % (pre, post))
                Trajectory(self.template, m, None).to_atoms().save_to_pdb(fname)
            out = True
        else:
            out = [
                StringIO.StringIO(
                    Trajectory(self.template, m, None).to_atoms().make_pdb()
                )
                for m in execution_mode[mode][0]
            ]
        return out

    def rmsf(self, chains=''):
        """
        Calculates the RMSF for each residue.
        :param chains: string chains for which RMSF should be calculated.
        :return: list of RMSF values.
        """
        mdls = self.select('chain ' + ','.join(chains))
        mdl_lth = len(mdls.template)
        mdls_crds = np.stack(mdls.coordinates.reshape(-1, mdl_lth, 3), axis=1)
        avg = [np.mean(rsd, axis=0) for rsd in mdls_crds]
        return [np.mean([np.linalg.norm(avg[i] - case) for case in rsd]) for i, rsd in enumerate(mdls_crds)]


if __name__ == '__main__':
    pass
