import numpy as np
import pandas as pd
from pykrige.ok3d import OrdinaryKriging3D

def krige_3d(df: pd.DataFrame, resolution: float = 5.0):

    # Extracting points and values
    x = df["X"].values
    y = df["Y"].values
    z = df["Z"].values
    r = df["R"].values

    # Defining regular grid
    grid_x = np.arange(x.min(), x.max(), resolution)
    grid_y = np.arange(y.min(), y.max(), resolution)
    grid_z = np.arange(z.min(), z.max(), resolution)
    Xg, Yg, Zg = np.meshgrid(grid_x, grid_y, grid_z, indexing="ij")

    # Creating kriging object
    ok3d = OrdinaryKriging3D(
        x, y, z, r,
        variogram_model="spherical" # to change @MaxSC4
    )

    # Apply kriging on the grid
    Rg, _ = ok3d.execute("grid", grid_x, grid_y, grid_z)

    return Xg, Yg, Zg, Rg

