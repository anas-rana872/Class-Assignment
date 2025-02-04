from scripts.update_blr_data import update_blr_data
from scripts.data_cleaning import clean_data

# File paths
file1_path = "data/file1.xlsx"
file2_path = "data/file2.xlsx"
json_path = "data/state_mapping.json"
output_path = "data/updated_file.xlsx"
cleaned_output_path = "data/cleaned_updated_file.xlsx"

if __name__ == "__main__":
    print("Updating file1 based on file2...")
    update_blr_data(file1_path, file2_path, output_path)

    print("Cleaning data and mapping state codes...")
    clean_data(output_path, json_path, cleaned_output_path)

    print("✅ Data processing completed successfully!")
