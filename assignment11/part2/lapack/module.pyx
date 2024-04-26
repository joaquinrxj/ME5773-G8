# cython: wraparound=False
# cython: boundscheck=False
# cython: profile=False
# cython: initializedcheck=False
import cython
cimport cython

import  numpy as np
cimport numpy as np

from libc.stdint cimport int64_t
from libc.stdlib cimport malloc, free


# This portuion is necessary when importing functions defined in c.
# see more in the files:
# /apps/intel/oneapi/mkl/latest/include/mkl.h
# /apps/intel/oneapi/mkl/latest/include/mkl_lapacke.h

cdef extern from "mkl.h" nogil:
    int LAPACKE_dgesv( int matrix_layout, int64_t n, int64_t nrhs,
                          double* a, int64_t lda, int64_t* ipiv,
                          double* b, int64_t ldb )
    int LAPACKE_dsysv( int matrix_layout, char uplo, int64_t n, 
                          int64_t nrhs, double* a, int64_t lda, 
                          int64_t* ipiv, double* b, int64_t ldb)
    int LAPACKE_dsysv_work( int matrix_layout, char uplo, int64_t n, 
                          int64_t nrhs, double* a, int64_t lda, 
                          int64_t* ipiv, double* b, int64_t ldb,
                          double* work, int64_t lwork)

def mkl_solver(double[:,::1] A, double[:,::1] B):
    """
    Function that uses MKL's LAPACK DESV routine to solve a general system
    of equations. This uses a LU factorization approach.

    The system solved has the form: AX = B

    INPUTS:
    - A: double array (n x n) with the coefficient matrix info.
    - B: double array (n x nrhs) with the right hand sides of the system.

    Note: This function overwrites the values in A and B.

    A is overwritten with the values of the LU decomposition.
    B is overwriten with the values of the solution.

    """
    cdef int64_t lda, ldb, n, nrhs, matrix_layout
    cdef int64_t[:] ipiv_memview, i
    
    matrix_layout = 101 # Row major

    lda = A.shape[1]
    ldb = B.shape[1]
    
    n = A.shape[0]
    nrhs = B.shape[1]
    
    # Use numpy to create the memory for the ipiv input.
    ipiv_memview = np.zeros(A.shape[0], dtype=np.int64)
    
    # Call LAPACK function imported from C library. 
    LAPACKE_dgesv( matrix_layout, n, nrhs,
                          &A[0,0], lda, &ipiv_memview[0],
                          &B[0,0], ldb )

# end function

def mkl_solver_symm(double[:,::1] A, double[:,::1] B, algorithm=None):
    """
    Function that uses MKL's LAPACK DESV routine to solve a general system
    of equations. This uses a LU factorization approach.

    The system solved has the form: AX = B

    INPUTS:
    - A: double array (n x n) with the coefficient matrix info.
    - B: double array (n x nrhs) with the right hand sides of the system.

    Note: This function overwrites the values in A and B.

    A is overwritten with the values of the LU decomposition.
    B is overwriten with the values of the solution.

    """
    cdef int64_t lda, ldb, n, nrhs, matrix_layout
    cdef int64_t[:] ipiv_memview, i
    cdef char uplo
    cdef double[:] work
    cdef int64_t lwork
    
    matrix_layout = 101 # Row major

    uplo = 'L'

    lda = A.shape[1]
    ldb = B.shape[1]
    
    n = A.shape[0]
    nrhs = B.shape[1]

    lwork = 1
    work=np.zeros(lwork)
    
    # Use numpy to create the memory for the ipiv input.
    ipiv_memview = np.zeros(A.shape[0], dtype=np.int64)
    
    # Call LAPACK function imported from C library. 

    if algorithm=='dsysv_work':
        LAPACKE_dsysv_work( matrix_layout, uplo, n, nrhs,
                              &A[0,0], lda, &ipiv_memview[0],
                              &B[0,0], ldb, &work[0], lwork )
    elif algorithm=='dsysv':
        LAPACKE_dsysv( matrix_layout, uplo, n, nrhs,
                      &A[0,0], lda, &ipiv_memview[0],
                      &B[0,0], ldb )
    else:
        LAPACKE_dsysv( matrix_layout, uplo, n, nrhs,
                      &A[0,0], lda, &ipiv_memview[0],
                      &B[0,0], ldb )
    # print(work[0])

# end function


