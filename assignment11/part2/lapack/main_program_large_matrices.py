import module as md
import numpy as np
import time
import scipy.linalg.lapack as scp


## Original Files With General Lapack Solver
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
# print(K)
# print(f)


t_start = time.time()
res = md.mkl_solver( K,f )
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Unsymmetric System: {0:.6f} s'.format(t_end-t_start))


## Lapck dsygv 

# Filling the Matrix and Vector according to instructions
K=np.zeros([N,N])
f=np.zeros([N,1])
for i in range(N-1):
    K[i,i]=2.0
    K[i+1,i]=-1.0
    # K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1,0]=1.0/N

print('Symmetric Solver (dsysv):')
# print(K)
# print(f)


t_start = time.time()
res = md.mkl_solver_symm( K,f ,'dsysv')
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Symmetric System (dsysv): {0:.6f} s'.format(t_end-t_start))


## Lapck dsygv_work 

# Filling the Matrix and Vector according to instructions
K=np.zeros([N,N])
f=np.zeros([N,1])
for i in range(N-1):
    K[i,i]=2.0
    K[i+1,i]=-1.0
    # K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1,0]=1.0/N

print('Symmetric Solver (dsysv_work):')
# print(K)
# print(f)


t_start = time.time()
res = md.mkl_solver_symm( K,f ,'dsysv_work')
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Symmetric System (dsysv_work): {0:.6f} s'.format(t_end-t_start))



## Scipy DGESV

# Filling the Matrix and Vector according to instructions
K=np.zeros([N,N])
f=np.zeros([N,1])
for i in range(N-1):
    K[i,i]=2.0
    K[i+1,i]=-1.0
    K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1,0]=1.0/N

print('UnSymmetric Solver scipy:')
# print(K)
# print(f)


t_start = time.time()
res = scp.dgesv( K,f, overwrite_a=True, overwrite_b=True)
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Unsymmetric System: {0:.6f} s'.format(t_end-t_start))


## Scipy DGSYSV

# Filling the Matrix and Vector according to instructions
K=np.zeros([N,N])
f=np.zeros([N,1])
for i in range(N-1):
    K[i,i]=2.0
    K[i+1,i]=-1.0
    # K[i,i+1]=-1.0
K[-1,-1]=1.0
f[-1,0]=1.0/N

print('Symmetric Solver :')
# print(K)
# print(f)


t_start = time.time()
res = scp.dsysv( K,f, overwrite_a=True, overwrite_b=True, lwork=1)
t_end = time.time()

print(K)
print(f)


print('Time spent on solving Symmetric System: {0:.6f} s'.format(t_end-t_start))






