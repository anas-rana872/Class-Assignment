import pandas as pd


def read_excel(file_path):
    """Reads an Excel file and returns a pandas DataFrame."""
    return pd.read_excel(file_path, engine='openpyxl')


def write_excel(df, file_path):
    """Writes a pandas DataFrame to an Excel file."""
    df.to_excel(file_path, index=False, engine='openpyxl')
