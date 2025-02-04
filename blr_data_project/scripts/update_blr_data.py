import pandas as pd
from utils.file_handler import read_excel, write_excel


def update_blr_data(file1_path, file2_path, output_path):
    """Updates file1 based on file2 by handling duplicates, updates, and additions."""

    # Load Data
    df1 = read_excel(file1_path)
    df2 = read_excel(file2_path)

    # Step 1: Remove exact duplicate rows from file2 based on 'blr_id' and 'blr_customer_params'
    df2 = df2.drop_duplicates(subset=['blr_id', 'blr_customer_params'])

    # Step 2: Identify rows where 'blr_id' is the same but 'blr_customer_params' is different
    common_ids = df1.merge(df2, on='blr_id', suffixes=('_file1', '_file2'))
    diff_params = common_ids[common_ids['blr_customer_params_file1'] != common_ids['blr_customer_params_file2']]

    # Update 'blr_customer_params' in df1 for matching 'blr_id'
    for _, row in diff_params.iterrows():
        df1.loc[df1['blr_id'] == row['blr_id'], 'blr_customer_params'] = row['blr_customer_params_file2']

    # Step 3: Add new rows from file2 to file1 if 'blr_id' is not present in file1
    new_rows = df2[~df2['blr_id'].isin(df1['blr_id'])]
    df1 = pd.concat([df1, new_rows], ignore_index=True)

    # Save updated data
    write_excel(df1, output_path)
    print(f"Updated data saved to {output_path}")
