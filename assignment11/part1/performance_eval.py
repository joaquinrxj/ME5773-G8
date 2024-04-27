import numpy as np
import searchUtilsTeam08 as search
import time

# Create an array with 10 million elements
large_array = np.linspace(-10, 10, 10**7, dtype=np.float64)

# The value to search for: the second to last element in the array
idx_search = large_array[-2]

# CPU time for the Fortran Linear Search algorithm
t_start = time.time()
idx_linear = search.searchutils.linearsearch(large_array, idx_search)
t_end = time.time()
print(f"Fortran linearSearch CPU time: {t_end - t_start} seconds")

# CPU time for the Fortran Binary Search algorithm
t_start = time.time()
idx_binary = search.searchutils.binarysearch(large_array, idx_search)
t_end = time.time()
print(f"Fortran binarySearch CPU time: {t_end - t_start} seconds")

# Evaluate the CPU time for numpy's searchsorted
t_start = time.time()
idx_np_searchsorted = np.searchsorted(large_array, idx_search)
t_end = time.time()
print(f"NumPy searchsorted CPU time: {t_end - t_start} seconds")

# Evaluate the CPU time for numpy's argwhere
t_start = time.time()
idx_np_argwhere = np.argwhere(large_array == idx_search)[0][0]
t_end = time.time()
print(f"NumPy argwhere CPU time: {t_end - t_start} seconds")

# Verify the results
print(f"Index found by linearSearch: {idx_linear}")
print(f"Index found by binarySearch: {idx_binary}")
print(f"Index found by NumPy searchsorted: {idx_np_searchsorted}")
print(f"Index found by NumPy where: {idx_np_argwhere}")