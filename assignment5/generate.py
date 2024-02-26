## Script for generate.py 
## Prepared By:
##              Joaquin Rodriguez
##              Juan Camilo Velasquez
import time as time
import numpy as np
import h5py

# Function to export matrix to CSV and measure time
def export_csv(matrix, filename, fmt='%d'):
    start_time = time.time()
    np.savetxt(filename, matrix, delimiter=',', fmt=fmt)
    elapsed_time = time.time() - start_time
    print(f"Time to generate and save {filename}: {elapsed_time:.6f} seconds")

    # Function to export matrix to NPZ and measure time
def export_npy(matrix, filename):
    start_time = time.time()
    np.save(filename, matrix)
    elapsed_time = time.time() - start_time
    print(f"Time to save {filename}: {elapsed_time:.6f} seconds")

def export_hdf5(matrix, dataset_name,group, filename, compression=None, chunks=None):
    with h5py.File(filename, 'a') as hdf5_file:
        start_time = time.time()
        grp = hdf5_file.require_group(group)
        #
        #dataset_name = "datasetCE"
        #
        #if dataset_name in grp:
        #    del grp[dataset_name]  # Delete the existing dataset if it already exists
        
        grp.create_dataset(dataset_name, data=matrix, compression=compression, chunks=chunks)
        
        elapsed_time = time.time() - start_time
        print(f"Time to create/update dataset in {dataset_name}: {elapsed_time:.6f} seconds")

# Matrix A
min_value_A = 2
max_value_A = 9
shape_A = (5000, 5000)
matrix_A = np.random.randint(min_value_A, max_value_A + 1, shape_A, dtype=np.int64)

#Finished Matrix A
print('Completed Matrix A = ',matrix_A)

# Export matrix A to CSV
export_csv(matrix_A, 'A.csv', fmt='%d')
# Export matrix A to NPY
export_npy(matrix_A, 'A.npy')



# Matrix B
min_value_B = 100
max_value_B = 127
shape_B = (5000, 5000)
matrix_B = np.random.randint(min_value_B, max_value_B + 1, shape_B, dtype=np.int8)

#Finished Matrix B
print('Completed Matrix B = ',matrix_B)

# Export matrix B to CSV
export_csv(matrix_B, 'B.csv', fmt='%d')
# Export matrix B to NPY
export_npy(matrix_B, 'B.npy')



# Matrix C
exact_value_C = 0.33333
shape_C = (5000, 5000)
matrix_C = np.full(shape_C, exact_value_C, dtype=np.float64, order='C')

#Finished Matrix C
print('Completed Matrix C = ',matrix_C)

# Export matrix C to CSV
export_csv(matrix_C, 'C.csv', fmt='%.18e')
# Export matrix C to NPY
export_npy(matrix_C, 'C.npy')



# Matrix D
min_value_D = 1001
max_value_D = 1100
shape_D = (10, 10)
matrix_D = np.arange(min_value_D, max_value_D + 1, dtype=np.int16).reshape(shape_D, order='F')

#Finished Matrix D
print('Completed Matrix D = ',matrix_D)

# Export matrix D to CSV
export_csv(matrix_D, 'D.csv', fmt='%d')
# Export matrix D to NPY
export_npy(matrix_D, 'D.npy')



# Matrix E
min_value_E = 350.0
max_value_E = 350.3
shape_E = (2, 2)
matrix_E = np.linspace(min_value_E, max_value_E, num=np.prod(shape_E), dtype=np.float32).reshape(shape_E, order='C')

#Finished Matrix E
print('Completed Matrix E = ',matrix_E)

# Export matrix E to CSV
export_csv(matrix_E, 'E.csv', fmt='%.7e')
# Export matrix E to NPY
export_npy(matrix_E, 'E.npy')



# HDF5 export
hdf5_filename = 'matrix_db.hdf5'

# Create "integer_group"
with h5py.File(hdf5_filename, 'w') as hdf5_file:
    hdf5_file.create_group('integer_group').attrs['description'] = 'Integer matrices group'

# Add matrices to "integer_group"
export_hdf5(matrix_A,'matrix_A', 'integer_group', hdf5_filename, compression='gzip', chunks=(500, 500))
export_hdf5(matrix_B,'matrix_B', 'integer_group', hdf5_filename, compression='gzip', chunks=(1000, 1000))
export_hdf5(matrix_D,'matrix_D', 'integer_group', hdf5_filename)

# Create "float_group"
with h5py.File(hdf5_filename, 'a') as hdf5_file:
    hdf5_file.create_group('float_group').attrs['description'] = 'Float matrices group'
export_hdf5(matrix_C,'matrix_C', 'float_group', hdf5_filename, compression='gzip')
export_hdf5(matrix_E,'matrix_E', 'float_group', hdf5_filename)

    # Measure the size of each file
import os

def get_file_size(filename):
    return os.path.getsize(filename) / (1024 * 1024)  # Convert to MB

files_to_measure = ['A.csv', 'B.csv', 'C.csv', 'D.csv', 'E.csv', 'A.npy', 'B.npy', 'C.npy', 'D.npy', 'E.npy', 'matrix_db.hdf5']

for filename in files_to_measure:
    size_mb = get_file_size(filename)
    print(f"File size of {filename}: {size_mb:.6f} MB")
