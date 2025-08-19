import pandas as pd

# Load your merged file
df = pd.read_csv(r"D:\WRF LIFTS\data\processed\merged.csv")

# Show first 5 rows
print(df.head())

# Show first 5 columns
print(df.iloc[:, :5].head())