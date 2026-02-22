# pip install pandas
import pandas as pd
import glob

# Path to your CSV files
csv_files = glob.glob("./test/*.csv")

dataframes = []
for f in csv_files:
    print(f)
    try:
        df = pd.read_csv(f, encoding='utf-8')
    except UnicodeDecodeError:
        print(f"UTF-8 failed for {f}, trying latin1...")
        df = pd.read_csv(f, encoding='latin1')
    dataframes.append(df)

combined = pd.concat(dataframes, ignore_index=True)
combined.to_csv("Combined.csv", index=False)
