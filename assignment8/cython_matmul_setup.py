from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("matmul_cython.pyx"),
    include_dirs=[np.get_include()]
)