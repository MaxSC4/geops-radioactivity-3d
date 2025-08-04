import os
import pandas as pd
import logging
from .config import DATA_DIR, DATA_FILE

def load_data():
    file_path = os.path.join(DATA_DIR, DATA_FILE)
    logging.info(f"Chargement des données depuis : {file_path}")

    try:
        df = pd.read_csv(file_path)
        expected_columns = {"X", "Y", "Z", "R"}
        if not expected_columns.issubset(df.columns):
            raise ValueError("Le fichier doit contenir les colonnes X, Y, Z, R.")
        logging.info(f"{len(df)} lignes chargées.")
        return df
    except Exception as e:
        logging.error(f"Erreur lors du chargement : {e}")
        raise
