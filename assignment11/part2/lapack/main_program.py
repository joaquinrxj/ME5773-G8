import module as md
import numpy as np
import time


## Original Files

A =  np.array([[    -5.86,  3.99,  -5.93,  -2.82,  7.69, ],
               [     3.99,  4.46,  2.58,  4.42,  4.61, ],
               [    -5.93,  2.58, -8.52,  8.57,  7.69, ],
               [    -2.82,  4.42,  8.57,  3.72,  8.07, ],
               [     7.69,  4.61,  7.69,  8.07,  9.83 ]])

b = np.array([[    1.32, -6.33, -8.77, ],
              [    2.22,  1.69, -8.33, ],
              [    0.12, -1.56, 9.54,],
              [   -6.41, -9.49, 9.56, ],
              [    6.33, -3.67, 7.48 ]])





print(A)
print(b)


t_start = time.time()
res = md.mkl_solver( A,b )
t_end = time.time()

print(A)
print(b)


print('Time spent on solving Unsymmetric System: {0:.6f} s'.format(t_end-t_start))


## Original Files dsysv

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
res = md.mkl_solver_symm( A,b ,'dsysv')
t_end = time.time()

print(A)
print(b)


print('Time spent on solving Symmetric System (dsysv): {0:.6f} s'.format(t_end-t_start))



## Original Files dsysv

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
res = md.mkl_solver_symm( A,b ,'dsysv_work')
t_end = time.time()

print(A)
print(b)


print('Time spent on solving Symmetric System (dsysv_work): {0:.6f} s'.format(t_end-t_start))

