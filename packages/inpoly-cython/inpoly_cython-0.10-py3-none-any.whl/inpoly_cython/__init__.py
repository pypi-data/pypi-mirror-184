#!python
#cython: language_level=3
import os
import numpy as np
cstring=r'''
#!python
#cython: language_level=3
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)  # deactivate bnds checking
@cython.wraparound(False)   # deactivate -.ve indexing
def _inpoly(np.ndarray[double, ndim=+2] vert,
            np.ndarray[double, ndim=+2] node,
        np.ndarray[np.int32_t, ndim=+2] edge,
        const double ftol, const double lbar):
    """
    _INPOLY: the local cython version of the crossing-number
    test. Loop over edges; do a binary-search for the first
    vertex that intersects with the edge y-range; crossing-
    number comparisons; break when the local y-range is met.

    Updated: 19 December, 2020

    Authors: Darren Engwirda, Keith Roberts

    """
    cdef size_t epos, jpos, inod, jnod, jvrt
    cdef double feps, veps
    cdef double xone, xtwo, xmin, xmax, xdel
    cdef double yone, ytwo, ymin, ymax, ydel
    cdef double xpos, ypos, mul1, mul2

    feps = ftol * (lbar ** +1)          # local bnds reltol
    veps = ftol * (lbar ** +1)

    cdef size_t vnum = vert.shape[0]
    cdef size_t enum = edge.shape[0]

    cdef np.ndarray[np.int8_t] stat = np.full(
        vnum, +0, dtype=np.int8)

    cdef np.ndarray[np.int8_t] bnds = np.full(
        vnum, +0, dtype=np.int8)

    cdef np.int8_t *sptr = &stat[+0]    # ptr to contiguous
    cdef np.int8_t *bptr = &bnds[+0]

#----------------------------------- compute y-range overlap
    cdef np.ndarray[Py_ssize_t] ivec = \
        np.argsort(vert[:, 1], kind = "quicksort")

    YMIN = node[edge[:, 0], 1] - veps

    cdef np.ndarray[Py_ssize_t] head = \
        np.searchsorted(
            vert[:, 1], YMIN, "left", sorter=ivec)

    cdef const Py_ssize_t *iptr = &ivec[+0]
    cdef const Py_ssize_t *hptr = &head[+0]

#----------------------------------- loop over polygon edges
    for epos in range(enum):

        inod = edge[epos, 0]            # unpack *this edge
        jnod = edge[epos, 1]

        xone = node[inod, 0]
        xtwo = node[jnod, 0]
        yone = node[inod, 1]
        ytwo = node[jnod, 1]

        xmin = min(xone, xtwo)          # compute edge bbox
        xmax = max(xone, xtwo)

        xmin = xmin - veps
        xmax = xmax + veps
        ymax = ytwo + veps

        xdel = xtwo - xone
        ydel = ytwo - yone

        edel = abs(xdel) + ydel

    #------------------------------- calc. edge-intersection
        for jpos in range(hptr[epos], vnum):

            jvrt = iptr[jpos]

            if bptr[jvrt]: continue

            xpos = vert[jvrt, 0]
            ypos = vert[jvrt, 1]

            if ypos >= ymax: break      # due to the y-sort

            if xpos >= xmin:
                if xpos <= xmax:
                #------------------- compute crossing number
                    mul1 = ydel * (xpos - xone)
                    mul2 = xdel * (ypos - yone)

                    if feps * edel >= abs(mul2 - mul1):
                #------------------- BNDS -- approx. on edge
                        bptr[jvrt] = 1
                        sptr[jvrt] = 1

                    elif (ypos == yone) and (xpos == xone):
                #------------------- BNDS -- match about ONE
                        bptr[jvrt] = 1
                        sptr[jvrt] = 1

                    elif (ypos == ytwo) and (xpos == xtwo):
                #------------------- BNDS -- match about TWO
                        bptr[jvrt] = 1
                        sptr[jvrt] = 1

                    elif (mul1 <= mul2) and (ypos >= yone) \
                            and (ypos < ytwo):
                #------------------- advance crossing number
                        sptr[jvrt] = 1 - sptr[jvrt]

            elif (ypos >= yone) and (ypos < ytwo):
            #----------------------- advance crossing number
                sptr[jvrt] = 1 - sptr[jvrt]

    return stat, bnds
'''
dirname = os.path.join(os.path.abspath(os.path.dirname(__file__)))
polyfile = os.path.join(dirname, 'inpoly_with_c.pyx')

try:
    if not os.path.exists(polyfile):
        with open(polyfile, mode='w', encoding='utf-8') as f:
            f.write(cstring)
    import pyximport

    pyximport.install(setup_args={"include_dirs": np.get_include()})

    import inpoly_with_c

    _inpoly = inpoly_with_c._inpoly
except Exception as fe:

    def _inpoly(vert, node, edge, ftol, lbar):
        """
        _INPOLY: the local pycode version of the crossing-number
        test. Loop over edges; do a binary-search for the first
        vertex that intersects with the edge y-range; crossing-
        number comparisons; break when the local y-range is met.

        """

        feps = ftol * (lbar**+1)
        veps = ftol * (lbar**+1)

        stat = np.full(vert.shape[0], False, dtype=np.bool_)
        bnds = np.full(vert.shape[0], False, dtype=np.bool_)

        # ----------------------------------- compute y-range overlap
        ivec = np.argsort(vert[:, 1], kind="quicksort")

        XONE = node[edge[:, 0], 0]
        XTWO = node[edge[:, 1], 0]
        YONE = node[edge[:, 0], 1]
        YTWO = node[edge[:, 1], 1]

        XMIN = np.minimum(XONE, XTWO)
        XMAX = np.maximum(XONE, XTWO)

        XMIN = XMIN - veps
        XMAX = XMAX + veps
        YMIN = YONE - veps
        YMAX = YTWO + veps

        YDEL = YTWO - YONE
        XDEL = XTWO - XONE

        EDEL = np.abs(XDEL) + YDEL

        ione = np.searchsorted(vert[:, 1], YMIN, "left", sorter=ivec)
        itwo = np.searchsorted(vert[:, 1], YMAX, "right", sorter=ivec)

        # ----------------------------------- loop over polygon edges
        for epos in range(edge.shape[0]):

            xone = XONE[epos]
            xtwo = XTWO[epos]
            yone = YONE[epos]
            ytwo = YTWO[epos]

            xmin = XMIN[epos]
            xmax = XMAX[epos]

            edel = EDEL[epos]

            xdel = XDEL[epos]
            ydel = YDEL[epos]

            # ------------------------------- calc. edge-intersection
            for jpos in range(ione[epos], itwo[epos]):

                jvrt = ivec[jpos]

                if bnds[jvrt]:
                    continue

                xpos = vert[jvrt, 0]
                ypos = vert[jvrt, 1]

                if xpos >= xmin:
                    if xpos <= xmax:
                        # ------------------- compute crossing number
                        mul1 = ydel * (xpos - xone)
                        mul2 = xdel * (ypos - yone)

                        if feps * edel >= abs(mul2 - mul1):
                            # ------------------- BNDS -- approx. on edge
                            bnds[jvrt] = True
                            stat[jvrt] = True

                        elif (ypos == yone) and (xpos == xone):
                            # ------------------- BNDS -- match about ONE
                            bnds[jvrt] = True
                            stat[jvrt] = True

                        elif (ypos == ytwo) and (xpos == xtwo):
                            # ------------------- BNDS -- match about TWO
                            bnds[jvrt] = True
                            stat[jvrt] = True

                        elif (mul1 <= mul2) and (ypos >= yone) and (ypos < ytwo):
                            # ------------------- advance crossing number
                            stat[jvrt] = not stat[jvrt]

                elif (ypos >= yone) and (ypos < ytwo):
                    # ----------------------- advance crossing number
                    stat[jvrt] = not stat[jvrt]

        return stat, bnds


def inpoly2(vert, node, edge=None, ftol=5.0e-14):
    """
        INPOLY2: compute "points-in-polygon" queries.

        INPOLY is licensed under the following terms:

    This program may be freely redistributed under the condition that the copyright notices (including this entire header) are not removed, and no compensation is received through use of the software. Private, research, and institutional use is free. You may distribute modified versions of this code UNDER THE CONDITION THAT THIS CODE AND ANY MODIFICATIONS MADE TO IT IN THE SAME FILE REMAIN UNDER COPYRIGHT OF THE ORIGINAL AUTHOR, BOTH SOURCE AND OBJECT CODE ARE MADE FREELY AVAILABLE WITHOUT CHARGE, AND CLEAR NOTICE IS GIVEN OF THE MODIFICATIONS. Distribution of this code as part of a commercial system is permissible ONLY BY DIRECT ARRANGEMENT WITH THE AUTHOR. (If you are not directly supplying this code to a customer, and you are instead telling them how they can obtain it for free, then you are not required to make any arrangement with me.)

    DISCLAIMER: Neither I nor: Columbia University, the Massachusetts Institute of Technology, the University of Sydney, nor the National Aeronautics and Space Administration warrant this code in any way whatsoever. This code is provided "as-is" to be used at your own risk.

        STAT = INPOLY2(VERT, NODE, EDGE) returns the "inside/ou-
        tside" status for a set of vertices VERT and a polygon
        NODE, EDGE embedded in a two-dimensional plane. General
        non-convex and multiply-connected polygonal regions can
        be handled. VERT is an N-by-2 array of XY coordinates to
        be tested. STAT is an associated N-by-1 boolean array,
        with STAT[II] = TRUE if VERT[II, :] is an inside point.

        The polygonal region is defined as a piecewise-straight-
        line-graph, where NODE is an M-by-2 array of polygon ve-
        rtices and EDGE is a P-by-2 array of edge indexing. Each
        row in EDGE represents an edge of the polygon, such that
        NODE[EDGE[KK, 0], :] and NODE[EDGE[KK, 2], :] are the
        coordinates of the endpoints of the KK-TH edge. If the
        argument EDGE is omitted it assumed that the vertices in
        NODE are connected in ascending order.

        STAT, BNDS = INPOLY2(..., FTOL) also returns an N-by-1
        boolean array BNDS, with BNDS[II] = TRUE if VERT[II, :]
        lies "on" a boundary segment, where FTOL is a floating-
        point tolerance for boundary comparisons. By default,
        FTOL ~ EPS ^ 0.85.

        --------------------------------------------------------

        This algorithm is based on a "crossing-number" test,
        counting the number of times a line extending from each
        point past the right-most end of the polygon intersects
        with the polygonal boundary. Points with odd counts are
        "inside". A simple implementation requires that each
        edge intersection be checked for each point, leading to
        O(N*M) complexity...

        This implementation seeks to improve these bounds:

      * Sorting the query points by y-value and determining can-
        didate edge intersection sets via binary-search. Given a
        configuration with N test points, M edges and an average
        point-edge "overlap" of H, the overall complexity scales
        like O(M*H + M*LOG(N) + N*LOG(N)), where O(N*LOG(N))
        operations are required for sorting, O(M*LOG(N)) operat-
        ions required for the set of binary-searches, and O(M*H)
        operations required for the intersection tests, where H
        is typically small on average, such that H << N.

      * Carefully checking points against the bounding-box asso-
        ciated with each polygon edge. This minimises the number
        of calls to the (relatively) expensive edge intersection
        test.

        Updated: 19 Dec, 2020

        Authors: Darren Engwirda, Keith Roberts

    """

    vert = np.asarray(vert, dtype=np.float64)
    node = np.asarray(node, dtype=np.float64)

    STAT = np.full(vert.shape[0], False, dtype=np.bool_)
    BNDS = np.full(vert.shape[0], False, dtype=np.bool_)

    if node.size == 0:
        return STAT, BNDS

    if edge is None:
        # ----------------------------------- set edges if not passed
        indx = np.arange(0, node.shape[0] - 1)

        edge = np.zeros((node.shape[0], +2), dtype=np.int32)

        edge[:-1, 0] = indx + 0
        edge[:-1, 1] = indx + 1
        edge[-1, 0] = node.shape[0] - 1

    else:
        edge = np.asarray(edge, dtype=np.int32)

    # ----------------------------------- prune points using bbox
    xdel = np.nanmax(node[:, 0]) - np.nanmin(node[:, 0])
    ydel = np.nanmax(node[:, 1]) - np.nanmin(node[:, 1])

    lbar = (xdel + ydel) / 2.0

    veps = lbar * ftol

    mask = np.logical_and.reduce(
        (
            vert[:, 0] >= np.nanmin(node[:, 0]) - veps,
            vert[:, 1] >= np.nanmin(node[:, 1]) - veps,
            vert[:, 0] <= np.nanmax(node[:, 0]) + veps,
            vert[:, 1] <= np.nanmax(node[:, 1]) + veps,
        )
    )

    vert = vert[mask]

    if vert.size == 0:
        return STAT, BNDS

    # ------------------ flip to ensure y-axis is the `long` axis
    xdel = np.amax(vert[:, 0]) - np.amin(vert[:, 0])
    ydel = np.amax(vert[:, 1]) - np.amin(vert[:, 1])

    lbar = (xdel + ydel) / 2.0

    if xdel > ydel:
        vert = vert[:, (1, 0)]
        node = node[:, (1, 0)]

    # ----------------------------------- sort points via y-value
    swap = node[edge[:, 1], 1] < node[edge[:, 0], 1]
    temp = edge[swap]
    edge[swap, :] = temp[:, (1, 0)]

    # ----------------------------------- call crossing-no kernel
    stat, bnds = _inpoly(vert, node, edge, ftol, lbar)

    # ----------------------------------- unpack array reindexing
    STAT[mask] = stat
    BNDS[mask] = bnds

    return STAT, BNDS