import module as md
import numpy as np
import time


## Original Files
# Creating a matrix K and a vector f
N=10000
K=np.zeros([N,N])
f=np.zeros([N,1])

# Filling the Matrix and Vector according to instructions
for i in range(N-1):
    K[i,i]=2.0
    K[i+1,i]=-1.0
    K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1,0]=1.0/N

print('Unsymmetric Solver :')
print(K)
print(f)


t_start = time.time()
res = md.mkl_solver( K,f )
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Unsymmetric System: {0:.6f} s'.format(t_end-t_start))


## Original Files

# Filling the Matrix and Vector according to instructions
N=10000
K=np.zeros([N,N])
f=np.zeros([N,1])
for i in range(N-1):
    K[i,i]=2.0
    # K[i+1,i]=-1.0
    K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1,0]=1.0/N

print('Symmetric Solver :')
K=K.copy()
f=f.copy()
print(K)
print(f)


t_start = time.time()
res = md.mkl_solver_symm( K,f )
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Symmetric System: {0:.6f} s'.format(t_end-t_start))

