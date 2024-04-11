# matmul_cython.pyx
import numpy as np
cimport numpy as np

def matmul_cython(double[:, :] A, double[:, :] B):
    cdef int n = A.shape[0]
    cdef int m = A.shape[1]
    cdef int p = B.shape[1]
    cdef double[:, :] C = np.empty((n, p), dtype=np.float64)

    for i in range(n):
        for j in range(p):
            C[i, j] = 0.0
            for k in range(m):
                C[i, j] += A[i, k] * B[k, j]

    return C