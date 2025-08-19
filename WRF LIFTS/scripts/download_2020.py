import cdsapi
import os

c = cdsapi.Client()

year = '2025'
months = ['03', '04', '05']  # March, April, May
days_in_month = {
    '03': 31,
    '04': 30,
    '05': 31
}

# Make sure directory exists
os.makedirs("data/raw", exist_ok=True)

for month in months:
    for day in range(1, days_in_month[month] + 1):
        day_str = f"{day:02d}"
        filename = f"data/raw/balloon_wind_{year}_{month}_{day_str}.nc"

        if os.path.exists(filename):
            print(f"✅ Already exists: {filename}")
            continue

        print(f"⬇️ Downloading: {filename}")

        try:
            c.retrieve(
                'reanalysis-era5-pressure-levels',
                {
                    'product_type': 'reanalysis',
                    'format': 'netcdf',
                    'variable': [
                        'u_component_of_wind',
                        'v_component_of_wind',
                    ],
                    'pressure_level': [
                        '20', '30', '50', '70', '100', '125', '150',
                        '175', '200', '225', '250', '300', '350', '400',
                        '450', '500', '550', '600', '650', '700', '750',
                        '775', '800', '825', '850', '875', '900', '925',
                        '950', '975', '1000'
                    ],
                    'year': year,
                    'month': month,
                    'day': day_str,
                    'time': [f'{h:02d}:00' for h in range(24)],
                    'area': [18.6, -67.5, 17.8, -65.3],  # Puerto Rico bounding box
                    'grid': [0.25, 0.25],
                },
                filename
            )
        except Exception as e:
            print(f"❌ Failed to download {year}-{month}-{day_str}: {e}")



# 'area': [18.6, -67.5, 17.8, -65.3],  # Puerto Rico bounding box