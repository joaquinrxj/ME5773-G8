import cupy as cp
import time as time
import numpy as np


defK_kernel = cp.RawKernel(r'''

extern "C" __global__
void defK( double* K, int ncols, int nrows) {
    /*
    This function defines a square matrix K (row-major format)
    with all elements in the diagonal as 4 and all elements 
    next to the diagonal as -2. The last element of the diagonal
    set to 2. All other elements are set to zero.
    INPUTS: 
    - K: Pointer to the memory in K.
    - nrows: Number of rows of the matrix
    - ncols: Number of columns of the matrix
    */
    // FYI: This is a comment
    
    /* and this is also a comment */

    // Define global indices of the threads along each direction.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;   
    
    // Check that the i, j location lies within the matrix dimensions.
    if ( ( i < nrows) && ( j < ncols ) ){
        
        // Define the contiguous global index of the matrix.
        // i.e the index to access a single data point from the main 
        // pointer in K 
        // Consider the global indices as follows
        //
        // I_local = [[(0,0),(0,1),(0,2)],  // i,j indices for K.
        //            [(1,0),(1,1),(1,2)],
        //            [(2,0),(2,1),(2,2)]]
        //
        // I_g = [[ 0, 1, 2],  // global contiguous indices for K.
        //        [ 3, 4, 5],
        //        [ 6, 7, 8]]
        //
        // we use long long type (int64) because the 
        // integer value gets very large.
        //

        long long g_indx = i * ncols + j ;    
        
        if (i == j) {
            // Last diagonal element condition
            if (i == nrows - 1) {
                K_p[g_index] = 2.0;
            } else {
                K_p[g_index] = 4.0;
            }
        } else if ((i == j + 1) || (i == j - 1)) {
            // Direct neighbors of diagonal elements
            K_p[g_index] = -2.0;
        } else {
            // All other elements
            K_p[g_index] = 0.0;
        }
        
    }

}

''', 'defK')

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 10

K = cp.empty((N,N),dtype = cp.float64)
f=cp.zeros((N,1),dtype = cp.float64)
f[-1,1]=1.0/N

# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
defK_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( K, K.shape[0],K.shape[1]))  # grid, block and arguments

# Solution to system of equations
u=cp.linalg.solve(K,f)
print(u)
t_end = time.time()

# Check the values in the matrix:
print(I)

print(f"Time spent creating the matrix: {t_end-t_start:.6f} s")
