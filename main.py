from src.load_data import load_radioactivity_data
from src.interpolation import krige_3d
from src.visualization import plot_volume

if __name__ == "__main__":
    df = load_radioactivity_data("data/data.csv")
    Xg, Yg, Zg, Rg = krige_3d(df, resolution=5.0)
    points = df[["X", "Y", "Z"]].values
    plot_volume(Xg, Yg, Zg, Rg, points=points, opacity=0.4)
