import numpy as np
import time
from cython_matmul_pyx import matmul_cython

def main ():
	n = [3, 10, 100, 1000]


	for n in sizes:
		A = np.random.rand(n, n).astype(np.float64)
		B = np.random.rand(n, n).astype(np.float64)

		# Time Cython implementation
		start_time = time.time()
		C_cython = matmul_cython(A, B)
		end_time_Cython = time.time() - start_time

		# Time Numpy dot function
		start_time = time.time()
		C_numpy = np.dot(A, B)
		end_time_Numpy = time.time() - start_time

		print(f"Cython time: {end_time_Cython:.5f} seconds")
		print(f"Numpy time: {end_time_Numpy:.5f} seconds")
