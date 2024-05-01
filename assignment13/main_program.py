import numpy as np
import pyvista as pv

# Create four quad elements, as follows:
#
points = np.array([[-2, 0, 0],
                   [0, 0, 0],
                   [2, 0, 0],
                   [-2, 2, 0],
                   [0, 2, 0], # Center point
                   [2, 2, 0],
                   [-2, 4, 0],
                   [0, 4, 0],
                   [2, 4, 0]], dtype=np.float64 )

npoints = points.shape[0]

# Each quad element is formed by 4 nodes, with the following order
#
cells = np.array([4, 0, 1, 4, 3,  # First quad
                  4, 1, 2, 5, 4,  # Second quad
                  4, 3, 4, 7, 6,  # Third quad
                  4, 4, 5, 8, 7])    # Fourth quad


# Number of cells
ncells = 4

# All cells are type quad, thus we only define for each
# cell, its correspondign type:
cell_type = pv.CellType.QUAD * np.ones(ncells,dtype=np.int8)

# The grid is created using all the cells
grid = pv.UnstructuredGrid(cells, cell_type, points)

# Adding Point data (e.g temperature field, velocity field)
# Adding scalar field "dcenter"
center_point = np.array([0, 2, 0])
dcenter = np.linalg.norm(points - center_point, axis=1)
grid['dcenter'] = dcenter


# Vector fields can also be added for point data. 
# Adding vector field "velocity"
velocity = np.zeros_like(points)
velocity[:, 0] = points[:, 1]
velocity[:, 1] = -points[:, 0]
grid['velocity'] = velocity

grid.save("mainquad.vtk")

grid.plot(show_edges=True)
