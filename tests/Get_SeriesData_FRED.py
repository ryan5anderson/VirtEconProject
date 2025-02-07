import pyfredapi as pf
import pandas as pd
import time
import json
import os

# Replace with your FRED API key
API_KEY = "8bc4e28ada12118ea9c031306e66482c"

# List of category IDs
category_ids = [34009, 33058, 51]

# Dictionary to store all series data
final_data = {}

# Loop through each category ID and fetch series metadata
for category_id in category_ids:
    series_data = pf.get_category_series(category_id=category_id, api_key=API_KEY)

    for series_id, series_info in series_data.items():
        print(f"Fetching data for series: {series_id}")  # Debugging print

        # Fetch actual time-series data for each series ID
        time_series = pf.get_series(series_id=series_id, api_key=API_KEY)

        if isinstance(time_series, pd.DataFrame):
            time_series = time_series.to_json(orient="table")  # Convert DataFrame to list of dictionaries

        # Store in nested dictionary
        final_data[series_id] = {
            "series_info": vars(series_info),  # Convert SeriesInfo object to dictionary
            "series_data": time_series  # This is likely a dictionary of time-series data
        }

        # Optional: Avoid hitting rate limits
        time.sleep(0.5)

print(final_data)

save_directory = r"C:/Users/Soull/OneDrive/Documents/VirtEcon2_Data"

file_path = os.path.join(save_directory, "fred_series_data.json")

with open(file_path, "w") as f:
    json.dump(final_data, f, indent=4)

print(f"Data collection complete. Saved to '{file_path}'.")
