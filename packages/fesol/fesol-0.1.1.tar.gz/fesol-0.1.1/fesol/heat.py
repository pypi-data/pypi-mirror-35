"""Heat solver module"""

import fenics as fe
import numpy as np
from .common import load_mesh2solver, extract_dof
import logging
from .interface import Interface

logging.getLogger('FFC').setLevel(logging.WARNING)
fe.parameters['reorder_dofs_serial'] = False


class HeatSolver(object):
    """FEniCS based heat module solver

    The module is capable for solving the following module:

    T_t - kappa/(rho*C) * T'' - f = 0, where

    kappa is the thermal conductive coefficient.
    rho is the density
    C is the specific heat

    The above equation can be solved with either
    Dirichlet or/and Neumann boundary conditions

    Limitations:
        parameters must be constant in space and time
    """

    def __init__(self, **kwargs):
        """Constructor"""
        self.rho = kwargs.pop('rho', 1.0)
        self.kappa = kwargs.pop('kappa', 1.0)
        self.Cp = kwargs.pop('Cp', 1.0)
        assert self.rho > 0.0 and self.kappa > 0.0 and self.Cp > 0.0
        self.steady = kwargs.pop('steady', False)
        self.time_order = kwargs.pop('time_order', 1)
        assert self.time_order == 1 or self.time_order == 2
        self.alpha = fe.Constant(self.kappa / (self.rho * self.Cp))
        self.dt = fe.Constant(0.0)
        self.mesh = None
        self.boundary_domain = None
        self.ds = None
        self.V = None
        self.V_vec = None
        self.Tk = None
        self.T = None
        self.Tbak = None
        self.Q = None
        self.dbcs = []
        self._output_file = kwargs.pop('output_file', None)
        self.a = None
        self.L = None
        self.t = 0.0
        self.flux = None
        self.T_amb = None
        self.h_coeff = None
        self.dbc_profiles = {}
        self.nbc_profiles = {}
        self.nbcs = []
        self.interfaces = {}
        self.tdep_face_dofs = {}
        self._has_tdep = False
        self.f = None
        self._f_call = None

    @property
    def output_file(self):
        return self._output_file

    @output_file.setter
    def output_file(self, filename):
        assert isinstance(filename, str), 'Filename must be string'
        self._output_file = filename

    def update_material_properties(self, **kwargs):
        self.rho = kwargs.pop('rho', 1.0)
        self.kappa = kwargs.pop('kappa', 1.0)
        self.Cp = kwargs.pop('Cp', 1.0)
        assert self.rho > 0.0 and self.kappa > 0.0 and self.Cp > 0.0
        self.alpha.assign(self.kappa / (self.rho * self.Cp))

    def load_mesh(self, filename, boundary_file=None, degree=1):
        """Load in the file"""
        load_mesh2solver(self, filename, boundary_file=boundary_file)
        self.ds = fe.Measure('ds', domain=self.mesh,
                             subdomain_data=self.boundary_domain)
        self.V = fe.FunctionSpace(self.mesh, 'P', degree)
        self.V_vec = fe.VectorFunctionSpace(self.mesh, 'P', degree)

    def set_initial_condition(self, values, **kwargs):
        """Set the IC"""
        if self.Tk is None:
            self.Tk = fe.Function(self.V)
        if isinstance(values, np.ndarray) or isinstance(values, float):
            self.Tk.vector()[:] = values
        elif isinstance(values, str):
            if values.endswith('.xml'):
                self.Tk = fe.Function(self.V, values)
            else:
                raise RuntimeError('Unsupported input')

    def define_source_term(self, values):
        if self.f is None:
            self.f = fe.Function(self.V)
        if isinstance(values, np.ndarray) or isinstance(values, float):
            self.f.vector()[:] = values
        else:
            assert False

    def define_source_term_profile(self, call_obj):
        if not callable(call_obj):
            raise RuntimeError('Must register a callable object')
        self._f_call = call_obj
        if self.f is None:
            self.f = fe.Function(self.V)

    def define_const_temperature_bd(self, tag, value):
        self.dbcs.append(
            fe.DirichletBC(
                self.V,
                fe.Constant(float(value)),
                self.boundary_domain, tag
            )
        )

    def define_temperature_profile_bd(self, tag, call_obj):
        """Register a callable object on boundary

        def call_obj(t=None, coord=None):
            return t*coord[0]+coord[1]
        """
        if not callable(call_obj):
            raise RuntimeError('Must register a callable object')
        if tag not in self.tdep_face_dofs:
            self.tdep_face_dofs[tag] = extract_dof(
                self.V,
                self.boundary_domain,
                tag
            )
        self.dbc_profiles[tag] = call_obj
        self.dbcs.append(
            fe.DirichletBC(
                self.V,
                fe.Constant(0.0),
                self.boundary_domain,
                tag
            )
        )
        if self.T is None:
            self.T = fe.Function(self.V)
        self.dbcs[-1].set_value(self.T)
        self._has_tdep = True

    def define_adiabatic_bd(self, tag):
        self.nbcs.append(tag)
        if self.flux is None:
            self.flux = fe.Function(self.V)

    def define_const_flux_bd(self, tag, value):
        self.nbcs.append(tag)
        if self.flux is None:
            self.flux = fe.Function(self.V)
        dofs = extract_dof(
            self.V,
            self.boundary_domain,
            tag
        )
        for i in dofs:
            self.flux.vector()[i] = float(value)

    def define_flux_profile_bd(self, tag, call_obj):
        """Register a callable object on boundary

        def call_obj(t=None, coord=None):
            return t*coord[0]+coord[1]
        """
        self.nbcs.append(tag)
        if not callable(call_obj):
            raise RuntimeError('Must register a callable object')
        if self.flux is None:
            self.flux = fe.Function(self.V)
        if tag not in self.tdep_face_dofs:
            self.tdep_face_dofs[tag] = extract_dof(
                self.V,
                self.boundary_domain,
                tag
            )
        self.nbc_profiles[tag] = call_obj
        self._has_tdep = True

    def _update_time_dep_bds(self, dt, **kwargs):
        if not self._has_tdep:
            return
        t_2 = self.t - 0.5 * (self.time_order - 1.0) * dt
        t = self.t
        init = kwargs.pop('init', False)
        if init:
            t = 0.0
        coords = self.V.tabulate_dof_coordinates().reshape(-1, self.mesh.topology().dim())
        for tag, bd in self.dbc_profiles.items():
            dofs = self.tdep_face_dofs[tag]
            for i in dofs:
                self.T.vector()[i] = bd(
                    t=t,
                    coord=coords[i]
                )
        for tag, bd in self.nbc_profiles.items():
            dofs = self.tdep_face_dofs[tag]
            for i in dofs:
                self.flux.vector()[i] = bd(
                    t=t_2,
                    coord=coords[i]
                )

    def update_source_term(self, values):
        if self.f is None:
            raise RuntimeError('must define source term first')
        if isinstance(values, np.ndarray) or isinstance(values, float):
            self.f.vector()[:] = values
        else:
            assert False

    def _update_source_term_time_dep(self, dt, **kwargs):
        if self._f_call is None:
            return
        t = self.t - 0.5 * (self.time_order - 1.0) * dt
        coords = self.V.tabulate_dof_coordinates().reshape(-1, self.mesh.topology().dim())
        for i in range(coords.shape[0]):
            self.f.vector()[i] = self._f_call(t=t, coord=coords[i])

    def define_temperature_interface(self, tag, init_values=None):
        if tag not in self.tdep_face_dofs:
            self.tdep_face_dofs[tag] = extract_dof(
                self.V,
                self.boundary_domain,
                tag
            )
        ldofs = self.tdep_face_dofs[tag]
        self.interfaces[tag] = Interface(
            tag=tag,
            ldofs=ldofs,
            itype='d',
            lconn=None
        )
        iface = self.interfaces[tag]
        self.dbcs.append(
            fe.DirichletBC(
                self.V,
                fe.Constant(0.0),
                self.boundary_domain,
                tag
            )
        )
        if self.T is None:
            self.T = fe.Function(self.V)
        self.dbcs[-1].set_value(self.T)
        if init_values is not None:
            assert isinstance(init_values, float) or isinstance(
                init_values, np.ndarray)
            if isinstance(init_values, float):
                buff = np.empty(ldofs.size, dtype=float)
                buff[:] = init_values
            else:
                buff = init_values
            iface.assign(buff)

    def define_flux_interface(self, tag, init_values=None):
        if tag not in self.tdep_face_dofs:
            self.tdep_face_dofs[tag] = extract_dof(
                self.V,
                self.boundary_domain,
                tag
            )
        ldofs = self.tdep_face_dofs[tag]
        self.interfaces[tag] = Interface(
            tag=tag,
            ldofs=ldofs,
            itype='n',
            lconn=None
        )
        iface = self.interfaces[tag]
        if self.flux is None:
            self.flux = fe.Function(self.V)
        if init_values is not None:
            assert isinstance(init_values, float) or isinstance(
                init_values, np.ndarray)
            if isinstance(init_values, float):
                buff = np.empty(ldofs.size, dtype=float)
                buff[:] = init_values
            else:
                buff = init_values
            iface.assign(buff)

    def define_robin_interface(self, tag, init_t=None, init_h=None):
        if tag not in self.tdep_face_dofs:
            self.tdep_face_dofs[tag] = extract_dof(
                self.V,
                self.boundary_domain,
                tag
            )
        ldofs = self.tdep_face_dofs[tag]
        self.interfaces[tag] = Interface(
            tag=tag,
            ldofs=ldofs,
            itype='r',
            lconn=None
        )
        iface = self.interfaces[tag]
        if self.T_amb is None:
            self.T_amb = fe.Function(self.V)
        if self.h_coeff is None:
            self.h_coeff = fe.Function(self.V)
        if init_t is not None:
            assert isinstance(init_t, float) or isinstance(init_t, np.ndarray)
            if isinstance(init_t, float):
                buff = np.empty(ldofs.size, dtype=float)
                buff[:] = init_t
            else:
                buff = init_t
            iface.assign(buff)
        if init_h is not None:
            assert isinstance(init_h, float) or isinstance(init_h, np.ndarray)
            if isinstance(init_h, float):
                buff = np.empty(ldofs.size, dtype=float)
                buff[:] = init_h
            else:
                buff = init_h
            iface.assign_h(init_h)

    def init_solver(self):
        """Initialize the solver"""
        u, v = fe.TrialFunction(self.V), fe.TestFunction(self.V)
        if self.steady:
            F = self.alpha * fe.dot(fe.grad(u), fe.grad(v)) * fe.dx
        else:
            if self.time_order == 1:
                F = (1.0 / self.dt) * (u - self.Tk) * v * fe.dx + \
                    self.alpha * fe.dot(fe.grad(u), fe.grad(v)) * fe.dx
            else:
                F = (1.0 / self.dt) * (u - self.Tk) * v * fe.dx + \
                    self.alpha * \
                    fe.dot(0.5 * fe.grad(self.Tk + u), fe.grad(v)) * fe.dx
        self.a, self.L = fe.lhs(F), fe.rhs(F)
        if self.f is not None:
            self.L += self.f * v * fe.dx
        # apply Neumann
        for ntag in self.nbcs:
            self.L += self.alpha * self.flux * v * self.ds(ntag)
        for iface in self.interfaces.values():
            if iface.is_dirichlet():
                continue
            if iface.is_neumann():
                self.L += self.alpha * self.flux * v * self.ds(iface.tag)
            elif iface.is_robin():
                self.a += self.alpha * self.h_coeff * \
                    u * v * self.ds(iface.tag)
                self.L += self.alpha * self.h_coeff * \
                    self.T_amb * v * self.ds(iface.tag)
        if self.T is None:
            self.T = fe.Function(self.V)
        self.Tbak = fe.Function(self.V)

    def _update_interfaces(self):
        for iface in self.interfaces.values():
            if iface.is_dirichlet():
                iface.put_temperature2solver(self, self.T)
            elif iface.is_neumann():
                iface.put_flux2solver(self, self.flux, self.kappa)
            else:
                iface.put_h2solver(self, self.h_coeff, self.kappa)
                iface.put_ambient_temp2solver(self, self.T_amb)

    def update_temperature_interface(self, tag, T):
        assert tag in self.interfaces
        iface = self.interfaces[tag]
        assert iface.is_dirichlet()
        iface.assign(T)

    def update_flux_interface(self, tag, flux):
        assert tag in self.interfaces
        iface = self.interfaces[tag]
        assert iface.is_neumann()
        iface.assign(flux)

    def update_robin_interface(self, tag, Ta, h_coeff):
        assert tag in self.interfaces
        iface = self.interfaces[tag]
        assert iface.is_robin()
        iface.assign(Ta)
        iface.assign_h(h_coeff)

    def advance(self, t, dt):
        """Advance to t with dt"""
        assert dt > 0.0
        self.t = t
        self._update_time_dep_bds(dt)
        self._update_source_term_time_dep(dt)
        self._update_interfaces()
        self.dt.assign(dt)
        A = fe.assemble(self.a)
        b = fe.assemble(self.L)
        [bc.apply(A, b) for bc in self.dbcs]
        fe.solve(A, self.T.vector(), b)
        self.Tk.assign(self.T)

    def get_interface_temperature(self, tag):
        assert tag in self.interfaces
        dofs = self.tdep_face_dofs[tag]
        return self.Tk.vector().get_local()[dofs]

    def get_interface_flux(self, tag):
        assert tag in self.interfaces
        iface = self.interfaces[tag]
        return iface.compute_flux(
            mesh=self.mesh,
            V=self.V_vec,
            ds=self.ds,
            T=self.Tk,
            kappa=self.kappa
        )

    def get_interface_h(self, tag):
        assert tag in self.interfaces
        iface = self.interfaces[tag]
        if not iface.has_operator():
            iface.project_normals(
                mesh=self.mesh,
                V=self.V_vec,
                ds=self.ds
            )
        return iface.get_delta_coeffs() * self.kappa

    def get_interface_ambient_temperature(self, tag, h_given=None):
        assert tag in self.interfaces
        # first get the wall temperature
        Twall = self.get_interface_temperature(tag)
        # then add the heat lost from wall temperature
        if h_given is not None:
            hh = h_given
        else:
            hh = self.get_interface_h(tag)
        return Twall + self.get_interface_flux(tag) / hh

    def get_interface_vertices(self, tag):
        assert tag in self.interfaces
        dofs = self.tdep_face_dofs[tag]
        return self.V.tabulate_dof_coordinates().reshape(
            -1,
            self.mesh.topology().dim())[dofs]

    def get_interface_dofs(self, tag):
        assert tag in self.interfaces
        return self.tdep_face_dofs[tag].copy()

    def get_temperature_solutions(self, dofs=None):
        if dofs is None:
            return self.Tk.vector().get_local()
        else:
            assert isinstance(dofs, np.ndarray)
            return self.Tk.vector().get_local()[dofs]

    def write(self):
        """Dump solutions to FEniCS's VTK system"""
        assert self._output_file is not None, 'No ouput file has been set up.'
        if isinstance(self._output_file, str):
            self._output_file = fe.File(self._output_file)
        self._output_file << (self.Tk, self.t)

    def backup(self):
        """Backup solutions"""
        self.Tbak.assign(self.Tk)

    def restore(self):
        """Restore solutions"""
        self.Tk.assign(self.Tbak)
