import pandas as pd

def load_radioactivity_data(filepath: str) -> pd.DataFrame:
    """_summary_
    Args:
        filepath (str): The path to the CSV file containing radioactivity data.

    Raises:
        ValueError: If the file does not contain the expected columns.

    Returns:
        pd.DataFrame: A DF containing the radioactivity data and coordinates.
    """
    df = pd.read_csv(filepath)
    expected_columns = ['X', 'Y', 'Z', 'R']
    if not all(col in df.columns for col in expected_columns):
        raise ValueError(f"File must contain colums: {expected_columns}")

    return df