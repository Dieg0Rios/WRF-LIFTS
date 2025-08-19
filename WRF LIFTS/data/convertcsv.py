import xarray as xr
import glob
import os
from tqdm import tqdm

# Config - Set these once
INPUT_FOLDER = r"D:\WRF LIFTS\data\raw"
OUTPUT_FOLDER = r"D:\WRF LIFTS\data\processed"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Auto-create folder

# Find only unprocessed files
all_nc_files = glob.glob(os.path.join(INPUT_FOLDER, "*.nc"))
pending_files = [
    f for f in all_nc_files
    if not os.path.exists(
        os.path.join(OUTPUT_FOLDER, os.path.basename(f).replace(".nc", ".csv"))
    )
]

print(f"📂 Found {len(all_nc_files)} NC files ({len(pending_files)} need processing)")

# Conversion with progress tracking
for nc_file in tqdm(pending_files, desc="Converting"):
    try:
        csv_name = os.path.basename(nc_file).replace(".nc", ".csv")
        output_path = os.path.join(OUTPUT_FOLDER, csv_name)
        
        # Pure conversion - no calculations!
        xr.open_dataset(nc_file).to_dataframe().to_csv(output_path)
        print(f"\n✅ Saved {csv_name}")  # Newline for clean tqdm output
    except Exception as e:
        print(f"\n❌ Failed {os.path.basename(nc_file)}: {str(e)}")

# Summary
print(f"\n🎉 Finished! Processed: {len(pending_files)} | Skipped: {len(all_nc_files)-len(pending_files)}")
print(f"CSV files ready in: {OUTPUT_FOLDER}")