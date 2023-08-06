"""The common module of FESOL"""

import fenics as fe
import numpy as np

dolfin_convert = 'dolfin-convert'


def load_mesh2solver(solver, filename, boundary_file=None):
    """Load mesh files to solver

    If boundary_file is given, then both filename and boundary_file are given
    as FEniCS "xml" file format.

    Note that for the boundary_file, 'size_t' marker is expected.

    Otherwise, filename must not be "xml" file. And we need dolfin-convert
    to convert other file formats into fenics "xml".

    Also please note that on P1 elements are supported in general (AS INPUT!)
    """

    if boundary_file is not None:
        solver.mesh = fe.Mesh(filename)
        solver.boundary_domain = fe.MeshFunction(
            'size_t', solver.mesh, boundary_file)
    else:
        import subprocess
        import pathlib
        new_file = filename.split('.')[0] + '.xml'
        if not pathlib.Path(new_file).is_file():
            try:
                subprocess.call([dolfin_convert, filename, new_file])
            except Exception:
                msg = 'Make sure dolfin-convert is' + \
                    ' valid by setting \"dolfin_convert\",' + \
                    ' also make sure the file format is supported by fenics.'
                raise RuntimeError(msg)
        boundary_file = filename.split('.')[0] + '_facet_region.xml'
        solver.mesh = fe.Mesh(new_file)
        solver.boundary_domain = fe.MeshFunction(
            'size_t', solver.mesh, boundary_file)


def extract_dof(V, subdomain, mark, rank=1):
    """Extract the dof map of a subdomain, given its mark

    for suquencial case, not work in parallel, ie PETSc
    return is the dof that stored in numpy ndarray of dtype int
    """
    if rank == 1:
        val = mark
    else:
        val = tuple([mark] * rank)
    bc = fe.DirichletBC(V, val, subdomain, mark)
    return np.sort(
        np.array([key for key in bc.get_boundary_values()], dtype=np.uintp))


def create_local_connectivity(num_nodes, lconn, ldofs_sorted):
    """Construct local connectivity table

    To couple with other codes, we need to provide the interface meshes. For
    non-meshless remapping methods, we need also to provide the mesh
    connectivity besides nodes
    """
    gshifts = np.zeros(num_nodes, dtype=int)
    for i in range(ldofs_sorted.size):
        gshifts[ldofs_sorted[i]] = ldofs_sorted[i] - i
    nodes = lconn.shape[1]
    for elem in range(lconn.shape[0]):
        for j in range(nodes):
            lconn[elem][j] -= gshifts[lconn[elem][j]]
    return lconn
