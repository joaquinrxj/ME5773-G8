import numpy as np
import math as mt
import numexpr as ne
import time as time


# Number of iterations
N=10**9
print('N = ',N)

# Calculate the step size
deltax=2./N


## For Loop Way
# Initialize the integral value
F1=0.
# Record start time
time1=time.time()
# Calculate the integral using a for loop
for i in range(N):
    xi=2/N*i-1
    fx=mt.sqrt(4.0-4.0*xi**2)
    F1 += fx*deltax
# Record end time
time2=time.time()
time3=time2-time1
# Print the execution time and result
print(f"Time elapsed For Loop: {time3:.6f} seconds")
print(f"Integral Results: {F1:.16f}")



## Numpy's vectorized functions
# Record start time
time1=time.time()
# Calculate x values using numpy
# i_vec=np.linspace(0,N-1,N,dtype='int')
i_vec = np.arange(N, dtype=int)
x_vec=(2*i_vec/N)-1
# Calculate F values using numpy
F_vec=np.sqrt(4.0-4.0*x_vec**2)
# Calculate the integral using numpy
F2=np.sum(F_vec*deltax)
# Record end time
time2=time.time()
time3=time2-time1
# Print the execution time and result
print(f"Time elapsed Numpy: {time3:.6f} seconds")
print(f"Integral Results: {F2:.16f}")


## Using numexpr evaluations
# Record start time
time1=time.time()
# Create an array of integers from 0 to N-1
i_vec = np.arange(N, dtype=int)
# Calculate x values using numexpr
x_vec=ne.evaluate('(2*i_vec/N)-1')
# Calculate F values using numexpr
F_vec=ne.evaluate('sqrt(4.0-4.0*x_vec**2)')
# Calculate the integral using numexpr
F3=ne.evaluate('sum(F_vec*deltax)')
# Record end time
time2=time.time()
time3=time2-time1
# Print the execution time and result
print(f"Time elapsed Numexpr: {time3:.6f} seconds")
print(f"Integral Results: {F3:.16f}")

