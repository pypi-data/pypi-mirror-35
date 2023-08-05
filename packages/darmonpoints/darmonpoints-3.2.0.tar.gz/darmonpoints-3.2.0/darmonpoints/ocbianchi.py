#########################################################################
#       Copyright (C) 2011 Cameron Franc and Marc Masdeu
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#                  http://www.gnu.org/licenses/
#########################################################################
from sage.structure.element import ModuleElement
from sage.modules.module import Module
from sage.matrix.constructor import Matrix
from sage.matrix.matrix_space import MatrixSpace
from copy import copy
from sage.rings.finite_rings.integer_mod_ring import Zmod
from sage.rings.all import Integer,Zp
from sage.rings.padics.factory import ZpCA
from sage.rings.power_series_ring import PowerSeriesRing
from sage.structure.unique_representation import UniqueRepresentation
from sage.rings.rational_field import QQ
from sage.rings.integer_ring import ZZ
from sage.rings.padics.padic_generic import pAdicGeneric
from sage.categories.pushout import pushout
from sage.rings.infinity import Infinity
from sage.structure.sage_object import load,save
from sage.categories.action import Action
import operator
from sage.modular.pollack_stevens.sigma0 import Sigma0,Sigma0ActionAdjuster
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.modules.free_module_element import FreeModuleElement_generic_dense


oo = Infinity

class our_adjuster(Sigma0ActionAdjuster):
    """
    Callable object that turns matrices into 4-tuples.

    EXAMPLES::

        sage: from sage.modular.btquotients.pautomorphicform import _btquot_adjuster
        sage: adj = _btquot_adjuster()
        sage: adj(matrix(ZZ,2,2,[1..4]))
        (4, 2, 3, 1)
    """
    def __call__(self, g):
        a,b,c,d = g.list()
        return tuple([d,b,c,a])


class OCBianchiDistributionElement(ModuleElement):
    r"""
    This class represents elements in an overconvergent Bianchi coefficient module.

    INPUT:

     - ``parent`` - An overconvergent coefficient module.

     - ``val`` - The value that it needs to store (default: 0). It can be another OCBianchiDistributionElement,
       in which case the values are copied. It can also be a column vector (or something
       coercible to a column vector) which represents the values of the element applied to
       the polynomials `1`, `x`, `y`, `x^2`, `xy`, `y^2`, ... ,`y^n`.

     - ``check`` - boolean (default: True). If set to False, no checks are done and ``val`` is
       assumed to be the a column vector.

    """
    def __init__(self,parent,val = 0,check = True):
        ModuleElement.__init__(self,parent)
        self._parent = parent
        self._depth = self._parent._depth
        if not check:
            self._val = val
        else:
            if isinstance(val,self.__class__):
                if val._parent._depth == parent._depth:
                    self._val = val._val
                else:
                    d = min([val.nrows(),parent.dimension()])
                    self._val = val._val.submatrix(0,0,nrows = d)

            elif isinstance(val, Vector_integer_dense) or isinstance(val, FreeModuleElement_generic_dense):
                self._val = MatrixSpace(self._parent._R, self._depth, 1)(0)
                for i,o in enumerate(val.list()):
                    self._val[i,0] = o
            else:
                try:
                    self._val = Matrix(self._parent._R,self._depth,1,val)
                except (TypeError, ValueError):
                    self._val= self._parent._R(val) * MatrixSpace(self._parent._R,self._depth,1)(1)
        self._moments = self._val

    def moment(self, ij):
        if isinstance(ij,tuple):
            idx = self._parent.index(ij)
        else:
            idx = ij
        return self._parent._Rmod(self._moments[idx,0])

    def __getitem__(self,ij):
        r"""

        """
        return self.moment(ij)

    def __setitem__(self,ij, val):
        r"""
        Sets the value of ``self`` on the polynomial `x^iy^j` to ``val``.

        INPUT:
        - ``r`` - an integer. The power of `x`.
        - ``val`` - a value.

        EXAMPLES:

        """
        if isinstance(ij,tuple):
            idx = self._parent.index(ij[0],ij[1])
        else:
            idx = ij
        self._val[idx,0] = val

    def element(self):
        r"""
        The element ``self`` represents.
        """
        tmp = self.matrix_rep()
        return [tmp[ii,0] for ii in range(tmp.nrows())]

    def list(self):
        r"""
        The element ``self`` represents.
        """
        return self.element()

    def matrix_rep(self,B=None):
        r"""
        Returns a matrix representation of ``self``.
        """
        #Express the element in terms of the basis B
        if B is None:
            B = self._parent.basis()
        A = Matrix(self._parent._R,self._parent.dimension(),self._parent.dimension(),[[b._val[ii,0] for b in B] for ii in range(self._depth)])
        tmp = A.solve_right(self._val)
        return tmp

    def _add_(self,y):
        r"""
        Add two elements.
        """
        val = self._val + y._val
        return self.__class__(self._parent, val, check=False)

    def _sub_(self,y):
        r"""
        Subtract two elements.
        """
        val = self._val - y._val
        return self.__class__(self._parent, val, check=False)

    def r_act_by(self,x):
        r"""
        Act on the right by a matrix.
        """
        return self._acted_upon_(x.adjoint(), False)

    def _acted_upon_(self, x, right_action): # Act by x on the left
        if right_action:
            return self._acted_upon_(x.adjoint(), False)
        else:
            R = self._parent._R
            A = self._parent._get_powers(x)
            tmp = A * self._val
            return self.__class__(self._parent, tmp, check = False)

    def _neg_(self):
        return self.__class__(self._parent,-self._val, check = False)

    def _rmul_(self, a):
        #assume that a is a scalar
        return self.__class__(self._parent,a*self._val, check = False)

    def _repr_(self):
        r"""
        Returns the representation of self as a string.
        """
        R = PowerSeriesRing(self._parent._R, num_gens=2, default_prec=self._val.nrows(), names='x,y')
        s = str(sum([R(self._val[idx,0]*self._parent.monomial_from_index(R,idx)) for idx in range(self._val.nrows())]))
        return s

    def __cmp__(self,other):
        return cmp(self._val,other._val)

    def __nonzero__(self):
        return self._val != 0

    def evaluate_at_poly(self,P,R = None,depth=None):
        r"""
        Evaluate ``self`` at a polynomial
        """
        p = self._parent._p
        if depth is None:
            depth = self._depth
        if R is None:
            try:
                R = pushout(P.parent().base_ring(),self.parent().base_ring())
            except AttributeError:
                R = self.parent().base_ring()
        return sum(R(self._val[self._parent.index(mon.degrees()),0]) * aij for aij,mon in zip(P.coefficients(), P.monomials()))

    def valuation(self,l=None):
        r"""
        The `l`-adic valuation of ``self``.

        INPUT: a prime `l`. The default (None) uses the prime of the parent.

        """
        if not self._parent.base_ring().is_exact():
            if(not l is None and l!=self._parent._Rmod.prime()):
                raise ValueError, "This function can only be called with the base prime"
            l = self._parent._Rmod.prime()
            return min([self._val[ii,0].valuation(l) for ii in range(self._val.nrows())])
        else:
            return min([self._val[ii,0].valuation(l) for ii in range(self._val.nrows())])

    def reduce_mod(self, N = None):
        if N is None:
            N = self.parent()._pN
        self._val = self._val.apply_map(lambda x: x % N)
        return self


class OCVn(Module,UniqueRepresentation):
    Element=OCVnElement
    r"""
    This class represents objects in the overconvergent approximation modules used to
    describe overconvergent p-adic automorphic forms. 

    INPUT:

     - ``n`` - integer 

     - ``R`` - ring

     - ``depth`` - integer (Default: None)

     - ``basis`` - (Default: None)


    AUTHORS:

    - Cameron Franc (2012-02-20)
    - Marc Masdeu (2012-02-20)
    """
    def __init__(self,p,depth):
        Module.__init__(self,base = ZZ)
        self._R = ZZ
        self._p = p
        self._Rmod = ZpCA(p,depth - 1)
        self._depth = depth
        self._pN = self._p**(depth - 1)
        self._cache_powers = dict()
        self._unset_coercions_used()
        self._Sigma0 = Sigma0(self._p, base_ring = self._Rmod, adjuster = our_adjuster())
        self.register_action(Sigma0Action(self._Sigma0,self))
        self._populate_coercion_lists_()
        self._index = dict()
        self._ij = []
        m = 0
        for n in range(depth):
            for i in range(n+1):
                self._ij.append((n-i,i))
                self._index[(n-i,i)] = m
                m += 1
        self._dimension = m
        self._PowerSeries = PowerSeriesRing(self._Rmod, default_prec = self._dimension,name='z')

    def index(self, ij)
        return self._index[ij]
    def ij_from_pos(self, n):
        return self._ij[n]
    def monomial_from_index(self, R, n):
        x, y = R.gens()
        i, j = self._ij[n]
        return x**i * y**j

    def Sigma0(self):
        return self._Sigma0

    def approx_module(self, M = None):
        if M is None:
            M = self.dimension()
        return MatrixSpace(self._R, M, 1)

    def clear_cache(self):
        del self._cache_powers
        self._cache_powers = dict()

    def is_overconvergent(self):
        return True

    def _an_element_(self):
        r"""
        """
        return OCVnElement(self,Matrix(self._R,self._dimension,1,range(1,self._dimension+1)), check = False)

    def _coerce_map_from_(self, S):
        # Nothing coherces here, except OCVnElement
        return False

    def _element_constructor_(self,x,check = True):
        #Code how to coherce x into the space
        #Admissible values of x?
        return OCVnElement(self, x)

    def acting_matrix(self, g, M):
        return self._get_powers(g).submatrix(0,0,M,M)

    def _get_powers(self,abcd,emb = None):
        abcd = tuple(abcd.list())
        try:
            return self._cache_powers[abcd]
        except KeyError:
            pass
        R = self._PowerSeries
        if emb is None:
            a,b,c,d = abcd
        else:
            a,b,c,d = emb(abcd).list()
        r = R([b,a])
        s = R([d,c])
        ratio = r * s**-1
        ratio = ratio.change_ring(ZZ)
        y = R(1).change_ring(ZZ)
        xlist = [1] + [0 for o in range(self._depth - 1)]
        for ii in range(1,self._depth):
            y *= ratio
            ylist = y.list()[:self._depth]
            xlist.extend(ylist)
            xlist.extend([ZZ(0) for o in range(self._depth - len(ylist))])
        x = Matrix(R.base_ring(),self._depth,self._depth, xlist).apply_map(ZZ)
        self._cache_powers[abcd] = x
        return x

    def _repr_(self):
        r"""
        This returns the representation of self as a string.
        """
        return "Space of %s-adic distributions with k=0 action and precision cap %s"%(self._p, self._dimension - 1)

    def prime(self):
        return self._p

    def basis(self):
        r"""
        A basis of the module.

        INPUT:

         - ``x`` - integer (default: 1) the description of the
           argument x goes here.  If it contains multiple lines, all
           the lines after the first need to be indented.

         - ``y`` - integer (default: 2) the ...

        """
        try: return self._basis
        except: pass
        self._basis=[OCVnElement(self,Matrix(self._R,self._dimension,1,{(jj,0):1},sparse=False),check = False) for jj in range(self._dimension)]
        return self._basis

    def base_ring(self):
        r"""
        This function returns the base ring of the overconvergent element.
        """
        return self._Rmod

    def depth(self):
        r"""
        Returns the depth of the module.
        """
        return self._depth

    def dimension(self):
        r"""
        Returns the dimension (rank) of the module.
        """
        return self._dimension

    def precision_cap(self):
        r"""
        """
        return self._depth

    def is_exact(self):
        return False

class Sigma0Action(Action):
    def __init__(self,G,M):
        Action.__init__(self,G,M,is_left = True,op = operator.mul)

    def _call_(self,g,v):
        return v._acted_upon_(g.matrix(), False)
