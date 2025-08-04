from src.logger import setup_logger
from src.data_loader import load_data

def main():
    setup_logger()
    import logging
    logging.info("Début du programme")

    df = load_data()
    logging.info("Prévisualisation des premières lignes :")
    logging.info("\n" + str(df.head()))

    logging.info("Fin du chargement des données")

if __name__ == "__main__":
    main()
