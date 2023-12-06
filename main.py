from functions import dbparser, get_serial
import os
import pandas as pd

input_directory = 'input'
output_excel = 'output/processed_data.xlsx'  # Specify the output Excel file path

# Create an Excel writer
with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        print(f"Processing: {file_path}")

        # Process the file
        result = dbparser(file_path)
        if result is not None:
            # Use filename as sheet name (or modify it if needed)
            sheet_name = get_serial(file_path)
            result.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Saved {filename} to sheet: {sheet_name}")
        else:
            print(f"Failed to process {file_path}")

# The Excel file is saved when you exit the 'with' block

