# pip install pandas
import pandas as pd
import os

# Folder containing your CSV files
csv_folder = ''  # ← Replace this with your folder path
output_excel = '.xlsx' # Replace with output file name

# Create a Pandas Excel writer using openpyxl engine
with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            csv_path = os.path.join(csv_folder, filename)
            sheet_name = os.path.splitext(filename)[0][:31]  # Excel sheet names max 31 chars
            df = pd.read_csv(csv_path)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"✅ All CSVs have been combined into '{output_excel}' with each as a separate sheet.")
