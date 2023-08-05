
from libc.stdlib cimport (
        calloc,
        free
)
from cpython cimport array
import array


cimport c_util

__doc__ = 'Simple DNA sequence metrics'


cdef extern from 'sm_seqmetric.h':
    int sm_maxRuns(char* seq, int seq_length, int* ret_arr)
    int sm_gcContent(char* seq, int length)
# end cdef

def maxRuns(object seq_obj):

    cdef char*          seq
    cdef Py_ssize_t     length
    cdef int*           runs_arr = NULL
    cdef list           out = []
    seq = c_util.obj_to_cstr_len(seq_obj, &length)
    runs_arr = <int*> calloc(6, sizeof(int))
    if runs_arr == NULL:
        raise OSError()
    sm_maxRuns(seq, length, runs_arr)
    for i in range(6):
        out.append(runs_arr[i])
    free(runs_arr)
    return out
# end def

def gcContent(object seq_obj):

    cdef char*          seq
    cdef Py_ssize_t     length
    cdef float          gc_content

    seq = c_util.obj_to_cstr_len(seq_obj, &length)
    gc_content = sm_gcContent(seq, length)

    return gc_content
# end def
