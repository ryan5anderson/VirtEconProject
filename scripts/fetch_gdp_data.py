import requests
import pandas as pd
import os

# FRED API Details
API_KEY = "8bc4e28ada12118ea9c031306e66482c"  # Replace with your FRED API Key
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

def fetch_gdp_data(series_id="GDP"):
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Convert to DataFrame
    observations = data.get("observations", [])
    df = pd.DataFrame(observations)
    df['date'] = pd.to_datetime(df['date'])
    df.rename(columns={"value": "GDP"}, inplace=True)
    df['GDP'] = pd.to_numeric(df['GDP'], errors='coerce')

    # Save to raw data directory
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/FRED_GDP.csv", index=False)
    print("FRED GDP data saved.")

fetch_gdp_data()