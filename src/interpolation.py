import numpy as np
from scipy.interpolate import griddata
import pandas as pd

def interpolate_radioactivity(df: pd.DataFrame, resolution: float = 5.0):
    """
    Interpolates 3D radiometric values using trilinear interpolation.

    Parameters:
        df (pd.DataFrame): Input data with columns ['X', 'Y', 'Z', 'R']
        resolution (float): Grid spacing in each dimension

    Returns:
        (Xg, Yg, Zg, Rg): 3D meshgrid arrays with interpolated R values
    """
    # Extract coordinates and values
    points = df[['X', 'Y', 'Z']].values
    values = df['R'].values

    # Create regular grid
    xi = np.arange(df['X'].min(), df['X'].max(), resolution)
    yi = np.arange(df['Y'].min(), df['Y'].max(), resolution)
    zi = np.arange(df['Z'].min(), df['Z'].max(), resolution)
    Xg, Yg, Zg = np.meshgrid(xi, yi, zi, indexing='ij')

    # Interpolation
    Rg = griddata(points, values, (Xg, Yg, Zg), method='nearest')

    return Xg, Yg, Zg, Rg
