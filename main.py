from src.load_data import load_radioactivity_data
from src.interpolation import interpolate_radioactivity
from src.visualization import plot_volume

if __name__ == "__main__":
    df = load_radioactivity_data("data/data.csv")
    Xg, Yg, Zg, Rg = interpolate_radioactivity(df, resolution=5.0)
    plot_volume(Xg, Yg, Zg, Rg, opacity=0.4, cmap="plasma")
