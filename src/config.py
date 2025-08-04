import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

DATA_FILE = "data.csv"

GRID_RESOLUTION = 1.0  # mètre

LOG_FILE = os.path.join(BASE_DIR, "radioactivite.log")
