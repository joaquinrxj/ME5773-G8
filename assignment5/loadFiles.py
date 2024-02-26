## Script for loadFiles.py 
## Prepared By:
##              Joaquin Rodriguez
##              Juan Camilo Velasquez
import time as time
import numpy as np
import h5py

def load_csv(filename):
    start_time = time.time()
    matrix = np.loadtxt(filename, delimiter=',')
    elapsed_time = time.time() - start_time
    print(f"Time to load CSV file '{filename}': {elapsed_time:.6f} seconds")
    return matrix, elapsed_time

def load_npy(filename):
    start_time = time.time()
    matrix = np.load(filename)
    elapsed_time = time.time() - start_time
    print(f"Time to load NPY file '{filename}': {elapsed_time:.6f} seconds")
    return matrix, elapsed_time

def load_hdf5(filename, group, dataset):
    with h5py.File(filename, 'r') as hdf5_file:
        db = hdf5_file[f'{group}/{dataset}']
        start_time = time.time()
        matrix = db[...]
        elapsed_time = time.time() - start_time
        print(f"Time to load HDF5 file '{filename}', group '{group}', dataset '{dataset}': {elapsed_time:.6f} seconds")
    return matrix, elapsed_time

# File paths for each matrix
csv_filename_A = 'A.csv'
npy_filename_A = 'A.npy'
csv_filename_B = 'B.csv'
npy_filename_B = 'B.npy'
csv_filename_C = 'C.csv'
npy_filename_C = 'C.npy'
csv_filename_D = 'D.csv'
npy_filename_D = 'D.npy'
csv_filename_E = 'E.csv'
npy_filename_E = 'E.npy'
hdf5_filename = 'matrix_db.hdf5'
hdf5_group = 'integer_group'
hdf5_dataset = 'datasetCE'

# Load matrices A to E
matrix_csv_A, time_csv_A = load_csv(csv_filename_A)
matrix_npy_A, time_npy_A = load_npy(npy_filename_A)
matrix_csv_B, time_csv_B = load_csv(csv_filename_B)
matrix_npy_B, time_npy_B = load_npy(npy_filename_B)
matrix_csv_C, time_csv_C = load_csv(csv_filename_C)
matrix_npy_C, time_npy_C = load_npy(npy_filename_C)
matrix_csv_D, time_csv_D = load_csv(csv_filename_D)
matrix_npy_D, time_npy_D = load_npy(npy_filename_D)
matrix_csv_E, time_csv_E = load_csv(csv_filename_E)
matrix_npy_E, time_npy_E = load_npy(npy_filename_E)

# Load HDF5 matrix
matrix_A, time_A = load_hdf5(hdf5_filename, 'integer_group', 'matrix_A')
matrix_B, time_B = load_hdf5(hdf5_filename, 'integer_group', 'matrix_B')
matrix_C, time_C = load_hdf5(hdf5_filename, 'float_group', 'matrix_C')
matrix_D, time_D = load_hdf5(hdf5_filename, 'integer_group', 'matrix_D')
matrix_E, time_E = load_hdf5(hdf5_filename, 'float_group', 'matrix_E')

# Save the loaded matrices and times to an Excel file
#data = {'Matrix': ['CSV A', 'NPY A', 'CSV B', 'NPY B', 'CSV C', 'NPY C', 'CSV D', 'NPY D', 'CSV E', 'NPY E', 'HDF5'],
#        'Load Time (seconds)': [time_csv_A, time_npy_A, time_csv_B, time_npy_B, time_csv_C, time_npy_C,
#                                 time_csv_D, time_npy_D, time_csv_E, time_npy_E, time_hdf5]}
#df = pd.DataFrame(data)

#df.to_excel('load_times.xlsx', index=False)