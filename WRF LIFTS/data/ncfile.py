import xarray as xr

file_path = r"D:\WRF LIFTS\data\raw\balloon_wind_2020_03_01.nc"

with xr.open_dataset(file_path) as ds:
    print("=== VARIABLES ===")
    print("Available data variables:")
    for var in ds.data_vars:
        print(f"- {var} (shape: {ds[var].shape})")
    
    print("\n=== DIMENSIONS ===")
    print("Dimension sizes:")
    for dim, size in ds.sizes.items():  # Using .sizes instead of .dims
        print(f"- {dim}: {size}")
    
    print("\n=== COORDINATE VALUES ===")
    for coord in ds.coords:
        try:
            # Handle 0-dimensional coordinates differently
            if ds[coord].values.ndim == 0:
                print(f"{coord}: {ds[coord].values} (scalar)")
            else:
                print(f"{coord}: First 3 values: {ds[coord].values[:3]}")
        except Exception as e:
            print(f"{coord}: Could not display values - {str(e)}")