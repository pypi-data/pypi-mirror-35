# -*- coding: utf-8 -*-
"""This module contains classes and functions related to the
construction of finite element matrices.

A library user is mainly interested in the following:

    - :class:`~skfem.assembly.InteriorBasis`
    - :class:`~skfem.assembly.FacetBasis`
    - :func:`~skfem.assembly.asm`
    - :func:`~skfem.assembly.bilinear_form`
    - :func:`~skfem.assembly.linear_form`

"""

import numpy as np
from scipy.sparse import coo_matrix
from skfem.quadrature import get_quadrature
from inspect import signature

from typing import NamedTuple, Optional, Dict, List

from numpy import ndarray


class GlobalBasis():
    """The finite element basis is evaluated at global quadrature points
    and cached inside this object.

    Please see the following implementations:

        - :class:`~skfem.assembly.InteriorBasis`, for basis functions inside elements
        - :class:`~skfem.assembly.FacetBasis`, for basis functions on element boundaries

    """

    n_dof: ndarray = np.array([])
    e_dof: ndarray = np.array([])
    f_dof: ndarray = np.array([])
    i_dof: ndarray = np.array([])
    t_dof: ndarray = np.array([])
    N: int = 0
    dofnames: List[str] = []

    def __init__(self, mesh, elem, mapping, intorder):
        if mapping is None:
            self.mapping = mesh.mapping()
        else:
            self.mapping = mapping

        self._build_dofnum(mesh, elem)
        self.elem = elem
        self.Nbfun = self.t_dof.shape[0]

        if intorder is None:
            self.intorder = 2*self.elem.maxdeg
        else:
            self.intorder = intorder

        self.dim = mesh.p.shape[0]
        self.nt = mesh.t.shape[1]

        self.mesh = mesh

        self.refdom = mesh.refdom
        self.brefdom = mesh.brefdom

    def _build_dofnum(self, mesh, element):
        # vertex dofs
        self.n_dof = np.reshape(np.arange(element.nodal_dofs * mesh.p.shape[1], dtype=np.int64),
                                (element.nodal_dofs, mesh.p.shape[1]), order='F')
        offset = element.nodal_dofs*mesh.p.shape[1]

        # edge dofs
        if mesh.dim() == 3: 
            self.e_dof = np.reshape(np.arange(element.edge_dofs
                                              * mesh.edges.shape[1],
                                              dtype=np.int64),
                                    (element.edge_dofs, mesh.edges.shape[1]),
                                    order='F') + offset
            offset = offset + element.edge_dofs*mesh.edges.shape[1]

        # facet dofs
        if mesh.dim() >= 2: # 2D or 3D mesh
            self.f_dof = np.reshape(np.arange(element.facet_dofs
                                              * mesh.facets.shape[1],
                                              dtype=np.int64),
                                    (element.facet_dofs, mesh.facets.shape[1]),
                                    order='F') + offset
            offset = offset + element.facet_dofs*mesh.facets.shape[1]

        # interior dofs
        self.i_dof = np.reshape(np.arange(element.interior_dofs
                                          * mesh.t.shape[1],
                                          dtype=np.int64),
                                (element.interior_dofs, mesh.t.shape[1]),
                                order='F') + offset

        # global numbering
        self.t_dof = np.zeros((0, mesh.t.shape[1]), dtype=np.int64)

        # nodal dofs
        for itr in range(mesh.t.shape[0]):
            self.t_dof = np.vstack((self.t_dof,
                                    self.n_dof[:, mesh.t[itr, :]]))

        # edge dofs
        if mesh.dim() == 3:
            for itr in range(mesh.t2e.shape[0]):
                self.t_dof = np.vstack((self.t_dof,
                                        self.e_dof[:, mesh.t2e[itr, :]]))

        # facet dofs
        if mesh.dim() >= 2:
            for itr in range(mesh.t2f.shape[0]):
                self.t_dof = np.vstack((self.t_dof,
                                        self.f_dof[:, mesh.t2f[itr, :]]))

        self.t_dof = np.vstack((self.t_dof, self.i_dof))

        self.N = np.max(self.t_dof) + 1
        self.dofnames = element.dofnames

    def complement_dofs(self, *D):
        return np.setdiff1d(np.arange(self.N), np.concatenate(D))

    def _get_dofs(self, submesh):
        """Return global DOF numbers corresponding to a Submesh."""
        class Dofs(NamedTuple):
            nodal: Dict[str, ndarray] = {}
            facet: Dict[str, ndarray] = {}
            edge: Dict[str, ndarray] = {}
            interior: Dict[str, ndarray] = {}

        n_dof = {}
        f_dof = {}
        e_dof = {}
        i_dof = {}
        offset = 0

        if submesh.p is not None:
            for i in range(self.n_dof.shape[0]):
                n_dof[self.dofnames[i]] = self.n_dof[i, submesh.p]
                offset += 1
        if submesh.facets is not None:
            for i in range(self.n_dof.shape[0]):
                f_dof[self.dofnames[i + offset]] = self.f_dof[i, submesh.facets]
                offset += 1
        if submesh.edges is not None:
            for i in range(self.n_dof.shape[0]):
                e_dof[self.dofnames[i + offset]] = self.e_dof[i, submesh.edges]
                offset += 1
        if submesh.t is not None:
            for i in range(self.n_dof.shape[0]):
                i_dof[self.dofnames[i + offset]] = self.i_dof[i, submesh.t]

        return Dofs(n_dof, f_dof, e_dof, i_dof)

    def get_dofs(self, submesh):
        """Return global DOF numbers corresponding to one or multiple
        Submeshes."""
        class Dofs(NamedTuple):
            nodal: Dict[str, ndarray] = {}
            facet: Dict[str, ndarray] = {}
            edge: Dict[str, ndarray] = {}
            interior: Dict[str, ndarray] = {}
        if type(submesh) is dict:
            return {key: self._get_dofs(submesh[key]) for key in submesh}
        else:
            return self._get_dofs(submesh)

    def init_gbasis(self, nvals, nqp, order):
        if order == 0:
            return np.empty((self.Nbfun, nvals, nqp))
        else:
            return np.empty((self.Nbfun,) + order*(self.dim,) + (nvals, nqp))

    def default_parameters(self):
        """This is used by assembler to get default parameters for 'w'"""
        raise NotImplementedError("Default parameters not implemented")

    def interpolate(self, w, derivative=False):
        """Interpolate a solution vector to quadrature points.

        Parameters
        ----------
        w : ndarray of size Ndofs
            A solution vector
        derivative : (optional, default=False) bool
            Return also the derivative

        Returns
        -------
        ndarray of size Nelems x Nqp
            Interpolated solution vector

        """
        nqp = len(self.W)

        if self.elem.order[0] == 0:
            W = np.zeros((self.nelems, nqp))
        elif self.elem.order[0] == 1:
            W = np.zeros((self.dim, self.nelems, nqp))
        else:
            raise Exception("Interpolation of this element order is not implemented.")

        for j in range(self.Nbfun):
            jdofs = self.t_dof[j, :]
            W += w[jdofs][:, None] \
                 * self.basis[0][j]

        if derivative:
            if self.elem.order[1] == 1:
                dW = np.zeros((self.dim, self.nelems, nqp))
            elif self.elem.order[1] == 2:
                dW = np.zeros((self.dim, self.dim, self.nelems, nqp))
            else:
                raise Exception("Interpolation of this element order is not implemented.")
            for j in range(self.Nbfun):
                jdofs = self.t_dof[j, :]
                for a in range(self.dim):
                    dW[a, :, :] += w[jdofs][:, None] \
                                   * self.basis[1][j][a]
            return W, dW
        return W

    def find_dofs(self, test=None, bc=None, boundary=True, dofrows=None,
                  check_vertices=True, check_facets=True, check_edges=True):
        """Helper function for finding DOF indices for BC's.

        Does not test for element interior DOFs since they are not typically
        included in boundary conditions! Uses DOF numbering of 'u' variable.

        Parameters
        ----------
        test : (optional, default=function returning True) lambda
            An anonymous function with Ndim arguments. If returns other than 0
            when evaluated at the DOF location, the respective DOF is included
            in the return set.
        bc : (optional, default=zero function) lambda
            The boundary condition value.
        boundary : (optional, default=True) bool
            Check only boundary DOFs.
        dofrows : (optional, default=None) np.array
            List of rows that are extracted from the DOF structures.
            For example, if each node/facet/edge contains 3 DOFs (say, in three
            dimensional problems x, y and z displacements) you can give [0, 1]
            to consider only two first DOFs.
        check_vertices : (optional, default=True) bool
            Include vertex dofs
        check_facets: (optional, default=True) bool
            Include facet dofs
        check_edges: (optional, default=True) bool
            Include edge dofs (3D only)

        Returns
        -------
        x : np.array
            Solution vector with the BC's
        I : np.array
            Set of DOF numbers set by the function

        """
        if test is None:
            if self.mesh.dim() == 1:
                test = lambda x: 0*x + True
            elif self.mesh.dim() == 2:
                test = lambda x, y: 0*x + True
            elif self.mesh.dim() == 3:
                test = lambda x, y, z: 0*x + True

        if bc is None:
            if self.mesh.dim() == 1:
                bc = lambda x: 0*x
            elif self.mesh.dim() == 2:
                bc = lambda x, y: 0*x
            elif self.mesh.dim() == 3:
                bc = lambda x, y, z: 0*x

        x = np.zeros(self.N)

        dofs = np.zeros(0, dtype=np.int64)
        locs = np.zeros((self.mesh.dim(), 0))

        if check_vertices:
            # handle nodes
            N = self.mesh.nodes_satisfying(test)
            if boundary:
                N = np.intersect1d(N, self.mesh.boundary_nodes())
            if dofrows is None:
                Ndofs = self.n_dof[:, N]
            else:
                Ndofs = self.n_dof[dofrows][:, N]

            Ndofx = np.tile(self.mesh.p[0, N], (Ndofs.shape[0], 1)).flatten()
            Ndofy = np.tile(self.mesh.p[1, N], (Ndofs.shape[0], 1)).flatten()
            if self.mesh.dim() == 3:
                Ndofz = np.tile(self.mesh.p[2, N], (Ndofs.shape[0], 1)).flatten()
                locs = np.hstack((locs, np.vstack((Ndofx, Ndofy, Ndofz))))
            else:
                locs = np.hstack((locs, np.vstack((Ndofx, Ndofy))))

            dofs = np.hstack((dofs, Ndofs.flatten()))

        if check_facets and self.f_dof.shape[0]>0:
            # handle facets
            F = self.mesh.facets_satisfying(test)
            if boundary:
                F = np.intersect1d(F, self.mesh.boundary_facets())
            if dofrows is None:
                Fdofs = self.f_dof[:, F]
            else:
                Fdofs = self.f_dof[dofrows][:, F]

            if self.mesh.dim() == 2:
                mx = 0.5*(self.mesh.p[0, self.mesh.facets[0, F]] +
                          self.mesh.p[0, self.mesh.facets[1, F]])
                my = 0.5*(self.mesh.p[1, self.mesh.facets[0, F]] +
                          self.mesh.p[1, self.mesh.facets[1, F]])
                Fdofx = np.tile(mx, (Fdofs.shape[0], 1)).flatten()
                Fdofy = np.tile(my, (Fdofs.shape[0], 1)).flatten()
                locs = np.hstack((locs, np.vstack((Fdofx, Fdofy))))
            else:
                mx = np.sum(self.mesh.p[0, self.mesh.facets[:, F]], axis=0)/self.mesh.facets.shape[0]
                my = np.sum(self.mesh.p[1, self.mesh.facets[:, F]], axis=0)/self.mesh.facets.shape[0]
                mz = np.sum(self.mesh.p[2, self.mesh.facets[:, F]], axis=0)/self.mesh.facets.shape[0]
                Fdofx = np.tile(mx, (Fdofs.shape[0], 1)).flatten()
                Fdofy = np.tile(my, (Fdofs.shape[0], 1)).flatten()
                Fdofz = np.tile(mz, (Fdofs.shape[0], 1)).flatten()
                locs = np.hstack((locs, np.vstack((Fdofx, Fdofy, Fdofz))))

            dofs = np.hstack((dofs, Fdofs.flatten()))

        if check_edges and self.e_dof.shape[0]>0:
            # handle edges
            if self.mesh.dim() == 3:
                E = self.mesh.edges_satisfying(test)
                if boundary:
                    E = np.intersect1d(E, self.mesh.boundary_edges())
                if dofrows is None:
                    Edofs = self.e_dof[:, E]
                else:
                    Edofs = self.e_dof[dofrows][:, E]

                mx = 0.5*(self.mesh.p[0, self.mesh.edges[0, E]] +
                          self.mesh.p[0, self.mesh.edges[1, E]])
                my = 0.5*(self.mesh.p[1, self.mesh.edges[0, E]] +
                          self.mesh.p[1, self.mesh.edges[1, E]])
                mz = 0.5*(self.mesh.p[2, self.mesh.edges[0, E]] +
                          self.mesh.p[2, self.mesh.edges[1, E]])

                Edofx = np.tile(mx, (Edofs.shape[0], 1)).flatten()
                Edofy = np.tile(my, (Edofs.shape[0], 1)).flatten()
                Edofz = np.tile(mz, (Edofs.shape[0], 1)).flatten()

                locs = np.hstack((locs, np.vstack((Edofx, Edofy, Edofz))))

                dofs = np.hstack((dofs, Edofs.flatten()))

        if self.mesh.dim() == 2:
            x[dofs] = bc(locs[0, :], locs[1, :])
        elif self.mesh.dim() == 3:
            x[dofs] = bc(locs[0, :], locs[1, :], locs[2, :])
        else:
            raise NotImplementedError("Method find_dofs not implemented " +
                                      "for the given dimension.")

        return x, dofs


class FacetBasis(GlobalBasis):
    """Global basis functions evaluated at integration points on the element
    boundaries.

    Attributes
    ----------
    phi : numpy array
        Global basis functions at global quadrature points.
    dphi : numpy array
        Global basis function derivatives at global quadrature points.
    X : numpy array of size Ndim x Nqp
        Local quadrature points.
    W : numpy array of size Nqp
        Local quadrature weights.
    nf : int
    dx : numpy array of size Nelems x Nqp
        Can be used in computing global integrals elementwise.
        For example, np.sum(u**2*dx, axis=1) where u is also
        a numpy array of size Nelems x Nqp.
    find : numpy array
        A list of facet indices.
    tind : numpy array
        A list of triangle indices.
    normals
    mapping : an object of type skfem.mapping.Mapping
    elem : an object of type skfem.element.Element
    Nbfun : int
        The number of basis functions.
    intorder : int
        The integration order
    dim : int
    nt : int
    mesh : an object of type skfem.mesh.Mesh
    refdom : string
    brefdom : string

    Examples
    --------

    FacetBasis object is a combination of Mesh, Element,
    and Mapping:

    >>> from skfem import *
    >>> from skfem.models.poisson import mass
    >>> m = MeshTri.init_symmetric()
    >>> e = ElementTriP1()
    >>> fb = FacetBasis(m, e, MappingAffine(m))

    The object is used in the assembly of bilinear and
    linear forms where the integral is over the boundary
    of the domain (or elements).

    >>> B = asm(mass, fb)
    >>> B.shape
    (5, 5)

    """
    def __init__(self, mesh, elem, mapping=None, intorder=None, side=None):
        super(FacetBasis, self).__init__(mesh, elem, mapping, intorder)

        self.X, self.W = get_quadrature(self.brefdom, self.intorder)

        # triangles where the basis is evaluated
        if side is None:
            self.find = np.nonzero(self.mesh.f2t[1, :] == -1)[0]
            self.tind = self.mesh.f2t[0, self.find]
        elif side == 0 or side == 1:
            self.find = np.nonzero(self.mesh.f2t[1, :] != -1)[0]
            self.tind = self.mesh.f2t[side, self.find]
        else:
            raise Exception("Parameter side must be 0 or 1. Facet shares only two elements.")

        # boundary refdom to global facet
        x = self.mapping.G(self.X, find=self.find)
        # global facet to refdom facet
        Y = self.mapping.invF(x, tind=self.tind)

        if hasattr(mesh, 'normals'):
            self.normals = np.repeat(mesh.normals[:, :, None], len(self.W), axis=2)
        else:
            # construct normal vectors from side=0 always
            Y0 = self.mapping.invF(x, tind=self.mesh.f2t[0, self.find]) # TODO check why without this works also (Y0 = Y)
            self.normals = self.mapping.normals(Y0, self.mesh.f2t[0, self.find], self.find, self.mesh.t2f)

        self.nf = len(self.find)

        self.basis = list(zip(*[self.elem.gbasis(self.mapping, Y, j, self.tind) for j in range(self.Nbfun)]))

        self.nelems = self.nf
        self.dx = np.abs(self.mapping.detDG(self.X, find=self.find)) * np.tile(self.W, (self.nelems, 1))

        self.t_dof = self.t_dof[:, self.tind] # TODO this is required for asm(). Check for other options.

    def default_parameters(self):
        return {'x':self.global_coordinates(),
                'h':self.mesh_parameters(),
                'n':self.normals}

    def global_coordinates(self):
        return self.mapping.G(self.X, find=self.find)

    def mesh_parameters(self):
        if self.mesh.dim() == 1:
            return 0.0
        else:
            return np.abs(self.mapping.detDG(self.X, self.find)) ** (1.0 / (self.mesh.dim() - 1))


class InteriorBasis(GlobalBasis):
    """Global basis functions evaluated at integration points inside the
    elements.

    Attributes
    ----------
    phi : numpy array
        Global basis functions at global quadrature points.
    dphi : numpy array
        Global basis function derivatives at global quadrature points.
    X : numpy array of size Ndim x Nqp
        Local quadrature points.
    W : numpy array of size Nqp
        Local quadrature weights.
    nelems : int
    dx : numpy array of size Nelems x Nqp
        Can be used in computing global integrals elementwise.
        For example, np.sum(u**2*dx, axis=1) where u is also
        a numpy array of size Nelems x Nqp.
    mapping : an object of the type skfem.mapping.Mapping
    elem : an object of the type skfem.element.Element
    Nbfun : int
    intorder : int
    dim : int
    nt : int
    mesh : an object of the type skfem.mesh.Mesh
    refdom : string
    brefdom : string

    Examples
    --------

    InteriorBasis object is a combination of Mesh, Element,
    and Mapping:

    >>> from skfem import *
    >>> from skfem.models.poisson import laplace
    >>> m = MeshTri.init_symmetric()
    >>> e = ElementTriP1()
    >>> ib = InteriorBasis(m, e, MappingAffine(m))

    The resulting objects are used in the assembly.

    >>> K = asm(laplace, ib)
    >>> K.shape
    (5, 5)

    """
    def __init__(self, mesh, elem, mapping=None, intorder=None):
        super(InteriorBasis, self).__init__(mesh, elem, mapping, intorder)

        self.X, self.W = get_quadrature(self.refdom, self.intorder)

        self.basis = list(zip(*[self.elem.gbasis(self.mapping, self.X, j) for j in range(self.Nbfun)]))

        self.nelems = self.nt
        self.dx = np.abs(self.mapping.detDF(self.X)) * np.tile(self.W, (self.nelems, 1))

    def default_parameters(self):
        return {'x':self.global_coordinates(),
                'h':self.mesh_parameters()}

    def global_coordinates(self):
        return self.mapping.F(self.X)

    def mesh_parameters(self):
        return np.abs(self.mapping.detDF(self.X)) ** (1.0 / self.mesh.dim())

    def refinterp(self, interp, Nrefs=1):
        """Refine and interpolate (for plotting)."""
        # mesh reference domain, refine and take the vertices
        meshclass = type(self.mesh)
        m = meshclass.init_refdom()
        m.refine(Nrefs)
        X = m.p

        # map vertices to global elements
        x = self.mapping.F(X)

        # interpolate some previous discrete function at the vertices
        # of the refined mesh
        w = 0.0*x[0]

        for j in range(self.Nbfun):
            basis = self.elem.gbasis(self.mapping, X, j)
            w += interp[self.t_dof[j, :]][:, None]*basis[0]

        nt = self.nt
        t = np.tile(m.t, (1, nt))
        dt = np.max(t)
        t += (dt+1)*np.tile(np.arange(nt), (m.t.shape[0]*m.t.shape[1], 1)).flatten('F').reshape((-1, m.t.shape[0])).T

        if X.shape[0]==1:
            p = np.array([x.flatten()])
        else:
            p = x[0].flatten()
            for itr in range(len(x)-1):
                p = np.vstack((p, x[itr+1].flatten()))

        M = meshclass(p, t, validate=False)

        return M, w.flatten()


def asm(kernel, ubasis, vbasis=None, w=None, dw=None, ddw=None, nthreads=1, assemble=True):
    """Assemble finite element matrices.

    Parameters
    ----------
    kernel : function handle
        See InteriorBasis or FacetBasis.
    ubasis : GlobalBasis
    vbasis : (optional) GlobalBasis
    w : (optional) ndarray
        Accessible in form definition as w.w.
    dw : (optional) ndarray
        Accessible in form definition as w.dw.
    ddw : (optional) ndarray
        Accessible in form definition as w.ddw.
    nthreads : (optional, default=1) int
        Number of threads to use in assembly. This is only
        useful if kernel is numba function compiled with
        nogil = True, see Examples.

    Examples
    --------

    Creating multithreadable kernel function.

    from numba import njit

    @njit(nogil=True)
    def assemble(A, ix, u, du, v, dv, w, dx):
        for k in range(ix.shape[0]):
            i, j = ix[k]
            A[i, j] = np.sum((du[j][0] * dv[i][0] +\
                              du[j][1] * dv[i][1] +\
                              du[j][2] * dv[i][2]) * dx, axis=1)
    assemble.bilinear = True

    """
    import threading
    from itertools import product

    if vbasis is None:
        vbasis = ubasis

    nt = ubasis.nelems
    dx = ubasis.dx

    class FormParameters(NamedTuple):
        x: ndarray
        h: ndarray
        n: Optional[ndarray] = None
        w: Optional[ndarray] = None
        dw: Optional[ndarray] = None
        ddw: Optional[ndarray] = None

    w = FormParameters(w=w, dw=dw, ddw=ddw, **ubasis.default_parameters())

    if kernel.bilinear:
        # initialize COO data structures
        data = np.zeros((vbasis.Nbfun, ubasis.Nbfun, nt))
        rows = np.zeros(ubasis.Nbfun * vbasis.Nbfun * nt)
        cols = np.zeros(ubasis.Nbfun * vbasis.Nbfun * nt)

        # create sparse matrix indexing
        for j in range(ubasis.Nbfun):
            for i in range(vbasis.Nbfun):
                # find correct location in data,rows,cols
                ixs = slice(nt * (vbasis.Nbfun * j + i), nt * (vbasis.Nbfun * j + i + 1))
                rows[ixs] = vbasis.t_dof[i, :]
                cols[ixs] = ubasis.t_dof[j, :]

        # create indices for linear loop over local stiffness matrix
        ixs = [i for j, i in product(range(ubasis.Nbfun), range(vbasis.Nbfun))]
        jxs = [j for j, i in product(range(ubasis.Nbfun), range(vbasis.Nbfun))]
        indices = np.array([ixs, jxs]).T

        # split local stiffness matrix elements to threads
        threads = [threading.Thread(target=kernel, args=(data, ij,
                                                         *ubasis.basis,
                                                         *vbasis.basis,
                                                         w, dx)) for ij
                   in np.array_split(indices, nthreads, axis=0)]

        # start threads and wait for finishing
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        if assemble:
            K = coo_matrix((np.transpose(data, (1, 0, 2)).flatten('C'), (rows, cols)),
                              shape=(vbasis.N, ubasis.N))
            K.eliminate_zeros()
            return K.tocsr()
        else:
            return (np.transpose(data, (1, 0, 2)).flatten('C'), (rows, cols))
    else:
        data = np.zeros((vbasis.Nbfun, nt))
        rows = np.zeros(vbasis.Nbfun * nt)
        cols = np.zeros(vbasis.Nbfun * nt)

        for i in range(vbasis.Nbfun):
            # find correct location in data,rows,cols
            ixs = slice(nt * i, nt * (i + 1))
            rows[ixs] = vbasis.t_dof[i, :]
            cols[ixs] = np.zeros(nt)

        indices = range(vbasis.Nbfun)

        threads = [threading.Thread(target=kernel, args=(data, ix, *vbasis.basis, w, dx)) for ix
                   in np.array_split(indices, nthreads, axis=0)]

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        return coo_matrix((data.flatten('C'), (rows, cols)),
                          shape=(vbasis.N, 1)).toarray().T[0]


def bilinear_form(form):
    """Bilinear form decorator.
    
    This decorator is used for defining bilinear forms that can be assembled
    using :func:`~skfem.assembly.asm`.

    """
    nargs = len(signature(form).parameters)
    if nargs == 5:
        def kernel(A, ix, u, du, v, dv, w, dx):
            for k in range(ix.shape[0]):
                i, j = ix[k]
                A[i, j] = np.sum(form(u[j], du[j], v[i], dv[i], w) * dx, axis=1)
    elif nargs == 7:
        def kernel(A, ix, u, du, ddu, v, dv, ddv, w, dx):
            for k in range(ix.shape[0]):
                i, j = ix[k]
                A[i, j] = np.sum(form(u[j], du[j], ddu[j], v[i], dv[i], ddv[i], w) * dx, axis=1)
    else:
        raise NotImplementedError("Given number of form arguments not supported.")
    kernel.bilinear = True
    return kernel


def linear_form(form):
    """Linear form decorator.
    
    This decorator is used for defining linear forms that can be assembled
    using :func:`~skfem.assembly.asm`.

    """
    nargs = len(signature(form).parameters)
    if nargs == 3:
        def kernel(b, ix, v, dv, w, dx):
            for i in ix:
                b[i] = np.sum(form(v[i], dv[i], w) * dx, axis=1)
    elif nargs == 4:
        def kernel(b, ix, v, dv, ddv, w, dx):
            for i in ix:
                b[i] = np.sum(form(v[i], dv[i], ddv[i], w) * dx, axis=1)
    else:
        raise NotImplementedError("Given number of form arguments not supported.")
    kernel.bilinear = False
    return kernel


if __name__ == "__main__":
    import doctest
    doctest.testmod()
