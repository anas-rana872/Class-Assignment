# import pandas as pd
from utils.file_handler import read_excel, write_excel
from utils.text_cleaner import clean_customer_params
from utils.state_mapper import map_state_codes


def clean_data(file_path, json_path, output_path):
    """Cleans customer params and maps state codes."""
    df = read_excel(file_path)

    # Clean 'blr_customer_params'
    df["blr_customer_params"] = df["blr_customer_params"].apply(clean_customer_params)

    # Map state codes
    df = map_state_codes(df, json_path)

    # Save the cleaned file
    write_excel(df, output_path)
    print(f"Cleaned data saved to {output_path}")
