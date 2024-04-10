import numpy as np
import time
from numba import jit, prange

@jit(nopython=True, parallel=True) #Adding decorators
def myfunct(x):
    """
    Defines the function to be integrated.

    INPUTS:
    - x: double, evaluation point.

    OUTPUTS:
    - double, evaluated function.
    
    """

    return np.sin(x*x)+x/2

# end function

@jit(nopython=True, parallel=True) #Adding decorators
def integral_riemann(a,b,N):
    """
    Implements the Riemann integration for the function
    myfunct(x).

    INPUTS:
    - a: double, Lower integration limit.
    - b: double, Upper integration limit.
    - N: Int, Number of integration regions.

    OUTPUTS:
    - double, evaluated integral.
    
    """
    dx = (b-a)/N
    F = 0
    
    for i in prange(N):
        x = a + i*dx
        F += myfunct(x)*dx
    # end for 

    return F

# end function

def run_experiment(num_threads):
    os.environ['NUMBA_NUM_THREADS'] = str(num_threads)
    t_start = time.time()
    a = 0
    b = 2
    N = 100_000_000  # 10**8 
    F = integral_riemann(a, b, N)
    t_end = time.time()

    return F, t_end - t_start

if __name__ == '__main__':
    num_threads_list = [1, 2, 4, 8, 16, 20]
    for num_threads in num_threads_list:
        F, cpu_time = run_experiment(num_threads)
        print(f'With {num_threads} threads:')
        print('Integral {0:f}'.format(F))
        print('CPU time:{0:.6f}s'.format(cpu_time))