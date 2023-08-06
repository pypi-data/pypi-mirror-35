"""A class that represents an interface of the physical model"""

import numpy as np
import fenics as fe

fe.parameters['reorder_dofs_serial'] = False


class Interface(object):

    def __init__(self, tag, ldofs, itype, **kwargs):
        self.tag = tag
        self.ldofs = ldofs
        self.itype = itype
        self.M = None
        # input values, t, flux, inf_t
        self.iv = np.zeros(ldofs.size, dtype=np.float64)
        self.ih = None
        if itype == 'r':
            self.ih = np.zeros(ldofs.size, dtype=np.float64)
        self.normals = None
        self.delta_coeffs = None
        self._has_proj_operator = False

    def is_dirichlet(self):
        return self.itype == 'd'

    def is_neumann(self):
        return self.itype == 'n'

    def is_robin(self):
        return self.itype == 'r'

    def has_operator(self):
        return self._has_proj_operator

    def compute_operator(self, mesh, V, ds):
        """Initialize the operator"""
        u, v = fe.TrialFunction(V), fe.TestFunction(V)
        self.M = fe.assemble(fe.inner(u, v) * ds(self.tag), keep_diagonal=True)
        self.M.ident_zeros()
        self.delta_coeffs = np.empty(self.ldofs.size, dtype=np.float64)
        self._has_proj_operator = True
        dim = mesh.topology().dim()
        normals = np.empty(dim * self.ldofs.size, dtype=np.float64)
        self.normals = normals.reshape(-1, dim)

    def project_normals(self, mesh, V, ds):
        if not self._has_proj_operator:
            self.compute_operator(mesh=mesh, V=V, ds=ds)
        v = fe.TestFunction(V)
        n = fe.FacetNormal(mesh)
        A = fe.FacetArea(mesh)
        buff = fe.assemble(A * fe.inner(n, v) * ds(self.tag))
        gnormals = fe.Function(V)
        fe.solve(self.M, gnormals.vector(), buff)
        dim = mesh.topology().dim()
        dofs = self.ldofs.size
        gnv = V.tabulate_dof_coordinates().size // dim // dim
        # np.set_printoptions(threshold=np.inf)
        # print(gnormals.vector().get_local().reshape(2,-1))
        for i in range(dim):
            j = i * gnv
            for p in range(dofs):
                index = int(self.ldofs[p] + j)
                self.normals[p][i] = gnormals.vector()[index]
        self.delta_coeffs[:] = 1.0 / \
            np.sqrt(np.sum(self.normals * self.normals, axis=1))

    def get_delta_coeffs(self):
        return self.delta_coeffs

    def assign(self, v):
        self.iv[:] = v

    def assign_h(self, h):
        self.ih[:] = h

    def compute_flux(self, mesh, V, ds, T, kappa):
        assert kappa > 0.0
        if self.M is None:
            self.project_normals(mesh, V, ds)
        dT = fe.project(fe.grad(T), V)
        dT = dT.vector().get_local()
        dim = mesh.topology().dim()
        dofs = self.ldofs.size
        gnv = V.tabulate_dof_coordinates().size // dim // dim
        flux = np.zeros(dofs, dtype=np.float64)
        for i in range(dim):
            j = i * gnv
            for p in range(dofs):
                index = int(self.ldofs[p] + j)
                flux[p] += self.normals[p][i] * dT[index]
        # scale
        return -kappa * self.delta_coeffs * flux

    def put_flux2solver(self, solver, F, kappa):
        k_inv = 1.0 / kappa
        # for i in range(self.ldofs.size):
        #     F.vector()[self.ldofs[i]] = self.iv[i] * k_inv
        F.vector()[self.ldofs] = self.iv * k_inv

    def put_temperature2solver(self, solver, T):
        for i in range(self.ldofs.size):
            T.vector()[self.ldofs[i]] = self.iv[i]

    def put_h2solver(self, solver, H, kappa):
        k_inv = 1.0 / kappa
        for i in range(self.ldofs.size):
            H.vector()[self.ldofs[i]] = self.ih[i] * k_inv

    def put_ambient_temp2solver(self, solver, Ta):
        self.put_temperature2solver(solver, Ta)

    def __hash__(self):
        return hash(self.tag)

    def __eq__(self, other):
        return self.tag == other.tag
