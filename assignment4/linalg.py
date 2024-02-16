## Script for Linear Algebra Operations
## Prepared By:
##              Joanquin Rodriguez
##              Juan Camilo Velasquez
import numpy as np
import time as time

# Define N as the Size of the Matrix
N=10000
print('N = ',N)

time1=time.time() # Start timing

# Creating a matrix K and a vector f
K=np.zeros([N,N])
f=np.zeros([N])

# Filling the Matrix and Vector according to instructions
for i in range(N-1):
    K[i,i]=2.0
    K[i+1,i]=-1.0
    K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1]=1.0/N

# Measuring time elasped for creating the matrix
time2=time.time() # End timing
time3=time2-time1 # Calculate elapsed time
print(f"Time elapsed Creating Arrays: {time3:.9f} seconds")

# Solving system of equations
time1=time.time() # Start timing
u = np.linalg.solve(K,f)
time2=time.time() # End timing
time3=time2-time1 # Calculate elapsed time
print(f"Time elapsed Solving: {time3:.9f} seconds")

print('Solution Vector = ',u)
print('Last Element of Solution Vector (U_n) = ',u[-1])
