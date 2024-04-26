import module as md
import numpy as np
import time


## Original Files

A =  np.array([[    6.8000,    -6.0500,    -0.4500,     8.3200,    -9.6700, ],
               [   -2.1100,    -3.3000,     2.5800,     2.7100,    -5.1400, ],
               [    5.6600,     5.3600,    -2.7000,     4.3500,    -7.2600, ],
               [    5.9700,    -4.4400,     0.2700,    -7.1700,     6.0800, ],
               [    8.2300,     1.0800,     9.0400,     2.1400,    -6.8700, ]])

b = np.array([[    4.0200,    -1.5600, ],
              [    6.1900,     4.0000, ],
              [   -8.2200,    -8.6700, ],
              [   -7.5700,     1.7500, ],
              [   -3.0300,     2.8600, ]])





print(A)
print(b)


t_start = time.time()
res = md.mkl_solver( A,b )
t_end = time.time()

print(A)
print(b)


print('Time spent on solving Unsymmetric System: {0:.6f} s'.format(t_end-t_start))


## Original Files

A =  np.array([[    -5.86,  0.00,  0.00,  0.00,  0.00, ],
               [     3.99,  4.46,  0.00,  0.00,  0.00, ],
               [    -5.93,  2.58, -8.52,  0.00,  0.00, ],
               [    -2.82,  4.42,  8.57,  3.72,  0.00, ],
               [     7.69,  4.61,  7.69,  8.07,  9.83 ]])

b = np.array([[    1.32, -6.33, -8.77, ],
              [    2.22,  1.69, -8.33, ],
              [    0.12, -1.56, 9.54,],
              [   -6.41, -9.49, 9.56, ],
              [    6.33, -3.67, 7.48 ]])





print(A)
print(b)


t_start = time.time()
res = md.mkl_solver_symm( A,b )
t_end = time.time()

print(A)
print(b)


print('Time spent on solving Symmetric System: {0:.6f} s'.format(t_end-t_start))

