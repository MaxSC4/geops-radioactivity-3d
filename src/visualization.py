# src/visualization.py

import pyvista as pv
import numpy as np

def plot_volume(Xg, Yg, Zg, Rg, opacity=0.4, cmap="viridis"):
    """
    Visualizes a 3D structured volume using PyVista.StructuredGrid.

    Parameters:
        Xg, Yg, Zg (np.ndarray): 3D meshgrids of coordinates
        Rg (np.ndarray): Interpolated scalar values
        opacity (float or list): Opacity for volume rendering
        cmap (str): Matplotlib colormap
    """
    # Flatten coordinates for StructuredGrid
    x = Xg.ravel(order="F")
    y = Yg.ravel(order="F")
    z = Zg.ravel(order="F")
    r = Rg.ravel(order="F")

    # Create the grid
    grid = pv.StructuredGrid()
    grid.points = np.c_[x, y, z]
    grid.dimensions = Xg.shape

    # Attach scalar data
    grid["Radioactivity"] = r

    # Plot
    plotter = pv.Plotter()
    plotter.add_mesh(grid, scalars="Radioactivity", cmap=cmap, opacity=opacity, show_scalar_bar=True)
    plotter.show()
