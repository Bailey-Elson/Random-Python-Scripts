# pip install pandas
import pandas as pd

# Change this to your Excel file path
excel_file = "Passenger import template harlow fields school 2025.xlsx"

# Read the Excel file (by default, reads the first sheet)
df = pd.read_excel(excel_file)

# Dictionary to store unique values for each column
unique_values = {}

for column in df.columns:
    unique_vals = df[column].dropna().unique().tolist()
    unique_values[column] = unique_vals

# Print results
for col, values in unique_values.items():
    print(f"Column: {col}")
    print(f"Unique Values: {values}")
    print("----")
