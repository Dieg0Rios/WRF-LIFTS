import pandas as pd
import glob

# Folder with all your CSVs
path = r"D:\WRF LIFTS\data\processed\*.csv"

# Get all CSV files in the folder
all_files = glob.glob(path)

# Read and combine
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Save as one big CSV
output_file = r"D:\WRF LIFTS\data\processed\merged.csv"
df.to_csv(output_file, index=False)

print(f"✅ Merge complete! Saved as {output_file}")