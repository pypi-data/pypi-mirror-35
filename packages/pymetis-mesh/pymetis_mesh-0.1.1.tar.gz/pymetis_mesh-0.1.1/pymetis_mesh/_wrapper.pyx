#!python
#cython: boundscheck=False, embedsignature=True, wraparound=False

"""METIS wrapper for partitioning `finite element` (FE) meshes

This module is designed to wrap around the two METIS routines for partitioning
FE meshes either in node-wise or element-wise setting. This routine is designed
to map to the original APIs with numpy ndarrays as input/output arguments.

Attributes
----------
OPTIONS: list of str
    tunable option parameters
PTYPE_RB: int
    Multilevel recursive bisectioning partitioning method
PTYPE_KWAY: int
    Multilevel k-way partitioning method
OBJTYPE_CUT: int
    Edge-cut minimization
OBJTYPE_VOL: int
    Total communication volume minimization
CTYPE_RM: int
    Random matching during coarsening
CTYPE_SHEM: int
    Sorted heavy-edge matching during coarsening
RTYPE_FM: int
    FM-based cut refinement
RTYPE_GREEDY: int
    Greedy-based cut and volume refinement
RTYPE_SEP2SIDED: int
    Two-sided node FM refinement
RTYPE_SEP1SIDED: int
    One-sided node FM refinement
"""

cimport numpy as np
import numpy as np
from ._version import __version__

__version__ = __version__
__author__ = 'Qiao Chen'
__copyright__ = 'Copyright 2018, Qiao Chen'


DEF NOPTIONS = 40


cdef extern from 'metis.h' nogil:
    ctypedef int idx_t
    ctypedef float real_t
    int nmbr 'METIS_OPTION_NUMBERING'
    int dbglvl 'METIS_OPTION_DBGLVL'
    int err_in 'METIS_ERROR_INPUT'
    int err_mem 'METIS_ERROR_MEMORY'
    int err 'METIS_ERROR'

    # APIs
    int METIS_PartMeshDual(
        idx_t *ne,
        idx_t *nn,
        idx_t *eptr,
        idx_t *eind,
        idx_t *vwgt,
        idx_t *vsize,
        idx_t *ncommon,
        idx_t *nparts,
        real_t *tpwgts,
        idx_t *options,
        idx_t *objval,
        idx_t *epart,
        idx_t *npart
    )
    int METIS_PartMeshNodal(
        idx_t *ne,
        idx_t *nn,
        idx_t *eptr,
        idx_t *eind,
        idx_t *vwgt,
        idx_t *vsize,
        idx_t *nparts,
        real_t *tpwgts,
        idx_t *options,
        idx_t *objval,
        idx_t *epart,
        idx_t *npart
    )
    int METIS_SetDefaultOptions(idx_t *options)

    # options
    int ptype 'METIS_OPTION_PTYPE'
    int objtype 'METIS_OPTION_OBJTYPE'
    int ctype 'METIS_OPTION_CTYPE'
    int rtype 'METIS_OPTION_RTYPE'
    int niter 'METIS_OPTION_NITER'
    int ufactor 'METIS_OPTION_UFACTOR'

    # option values

    int ptype_rb 'METIS_PTYPE_RB'
    int ptype_kway 'METIS_PTYPE_KWAY'

    int objtype_cut 'METIS_OBJTYPE_CUT'
    int objtype_vol 'METIS_OBJTYPE_VOL'
    int objtype_node 'METIS_OBJTYPE_NODE'

    int ctype_rm 'METIS_CTYPE_RM'
    int ctype_shem 'METIS_CTYPE_SHEM'

    int rtype_fm 'METIS_RTYPE_FM'
    int rtype_greedy 'METIS_RTYPE_GREEDY'
    int rtype_sep2sided 'METIS_RTYPE_SEP2SIDED'
    int rtype_sep1sided 'METIS_RTYPE_SEP1SIDED'


class MetisInputError(AttributeError):
    pass


class MetisMemoryError(MemoryError):
    pass


class MetisError(RuntimeError):
    pass


OPTIONS = ['ptype', 'objtype', 'ctype', 'rtype', 'niter', 'ufactor']

PTYPE_RB = ptype_rb
PTYPE_KWAY = ptype_kway

OBJTYPE_CUT = objtype_cut
OBJTYPE_VOL = objtype_vol
OBJTYPE_NODE = objtype_node

CTYPE_RM = ctype_rm
CTYPE_SHEM = ctype_shem

RTYPE_FM = rtype_fm
RTYPE_GREEDY = rtype_greedy
RTYPE_SEP2SIDED = rtype_sep2sided
RTYPE_SEP1SIDED = rtype_sep1sided


def part_mesh(int nv, idx_t[::1] eptr not None, idx_t[::1] eind not None,
    int nparts, *, int ncommon=1, idx_t[::1] vwgt=None, idx_t[::1] vsize=None,
    real_t[::1] tpwgts=None, one_base=False, elemental=True, debug=0,
    idx_t[::1] epart=None, idx_t[::1] npart=None, **ops):
    """The main partition interface

    Parameters
    ----------
    nv : int
        number of nodes
    eptr : memory view
        element pointer array, size of ne-1, where ne is the number of elements
    eind : memory view
        flattened connectivity table
    nparts : int
        number of partitions
    ncommon : int (optional)
        number of shared nodes that forms a cut, elemental part only
    vwgt : memory view (optional)
        weights of primary entity type
    vsize : memory view (optional)
        communication volumes of primary entity type
    tpwgts : memory view (optional)
        weights for partitions
    one_base : bool (optional)
        ``True`` if using Fortran-based index
    elemental : bool (optional)
        ``True`` if doing element-based partition
    debug: int (optional)
        debug level
    epart : memory view (optional)
        buffer output of element partition
    npart : memory view (optional)
        buffer output of node partition

    Returns
    -------
    dict with keys ``cuts``, ``epart``, ``npart``
        cuts, epart, npart

    Examples
    --------
    >>> from pymetis_mesh import *
    >>> import numpy as np
    >>> eptr = np.asarray([0, 3, 6], dtype='int32')
    >>> # two triangles, 4 nodes
    >>> eind = np.asarray([0, 1, 2, 0, 2, 3], dtype='int32')
    >>> outputs = part_mesh(4, eptr, eind, 2) # elemental wise two-part
    """
    cdef:
        # inputs
        idx_t _nparts = nparts
        idx_t _ncommon = ncommon
        idx_t _ne = len(eptr) - 1
        idx_t _nv = nv
        idx_t *_vwgt = &vwgt[0] if vwgt is not None else NULL
        idx_t *_vsize = &vsize[0] if vsize is not None else NULL
        real_t *_tpwgts = &tpwgts[0] if tpwgts is not None else NULL
        idx_t opts[NOPTIONS]
        int ret
        int dbg = <int> debug
        # outputs
        idx_t objval
        np.ndarray[np.int32_t, ndim=1] _epart
        np.ndarray[np.int32_t, ndim=1] _npart
    assert _nparts > 0
    assert _vwgt == NULL or (len(vwgt) == _ne and elemental) or len(vwgt) == _nv
    assert _vsize == NULL or (len(vsize) == _ne and elemental) or len(vwgt) == _nv
    assert _tpwgts == NULL or len(tpwgts) == _nparts
    assert dbg >= 0
    if epart is None:
        _epart = np.empty(_ne, dtype=np.int32)
    else:
        assert len(epart) == _ne
        _epart = np.asarray(epart)
    if npart is None:
        _npart = np.empty(_nv, dtype=np.int32)
    else:
        assert len(npart) == _nv
        _npart = np.asarray(npart)
    # set default options
    METIS_SetDefaultOptions(opts)
    opts[nmbr] = 1 if one_base else 0
    if dbg:
        opts[dbglvl] = dbg
    # parse options
    _ptype = ops.pop('ptype', None)
    if _ptype is not None:
        if _ptype != PTYPE_RB and _ptype != PTYPE_KWAY:
            raise MetisInputError('unknown ptype %r' % _ptype)
        opts[ptype] = <int> _ptype
    _objtype = ops.pop('objtype', None)
    if _objtype is not None:
        if _objtype != OBJTYPE_CUT and _objtype != OBJTYPE_VOL\
            and _objtype != OBJTYPE_NODE:
            raise MetisInputError('unknown objtype %r' % _objtype)
        opts[objtype] = <int> _objtype
    _ctype = ops.pop('ctype', None)  # coarsen
    if _ctype is not None:
        if _ctype != CTYPE_RM and _ctype != CTYPE_SHEM:
            raise MetisInputError('unknown ctype %r' % _ctype)
        opts[ctype] = <int> _ctype
    _rtype = ops.pop('rtype', None)  # refine
    if _rtype is not None:
        if _rtype != RTYPE_FM and _rtype != RTYPE_GREEDY \
            and _rtype != RTYPE_SEP2SIDED and _rtype != RTYPE_SEP1SIDED:
            raise MetisInputError('unknown rtype %r' % _rtype)
        opts[rtype] = <int> _rtype
    _niter = ops.pop('niter', None)
    if _niter is not None:
        opts[niter] = <int> _niter
    _ufactor = ops.pop('ufactor', None)
    if _ufactor is not None:
        opts[ufactor] = <int> _ufactor
    if elemental:
        ret = METIS_PartMeshDual(&_ne, &_nv, <idx_t *> &eptr[0],
            <idx_t *> &eind[0], _vwgt, _vsize, &_ncommon, &_nparts, _tpwgts,
            opts, &objval, <idx_t *> _epart.data, <idx_t *> _npart.data)
    else:
        ret = METIS_PartMeshNodal(&_ne, &_nv, <idx_t *> &eptr[0],
            <idx_t *> &eind[0], _vwgt, _vsize, &_nparts, _tpwgts, opts, &objval,
            <idx_t *> _epart.data, <idx_t *> _npart.data)
    if ret == 1:
        return {'cuts': objval, 'epart': _epart, 'npart': _npart}
    elif ret == err_in:
        raise MetisInputError('invalid input arguments')
    elif ret == err_mem:
        raise MetisMemoryError('bad alloc')
    else:
        raise MetisError('routine didn\'t return METIS_OK')
