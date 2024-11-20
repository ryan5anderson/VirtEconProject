# Import necessary libraries
import pandas as pd

# Load the dataset from the raw directory
file_path = "data/raw/FRED_gdp.csv"
gdp_df = pd.read_csv(file_path)

# Select and rename necessary columns
gdp_df = gdp_df[['date', 'GDP']]  # Keep only 'date' and 'GDP' columns
gdp_df.rename(columns={'date': 'DATE'}, inplace=True)

# Process the data
gdp_df['DATE'] = pd.to_datetime(gdp_df['DATE'])  # Convert DATE to datetime
gdp_df['Year'] = gdp_df['DATE'].dt.year          # Extract year
gdp_df['Quarter'] = gdp_df['DATE'].dt.quarter    # Extract quarter

# Calculate GDP Growth Rate
gdp_df['GDP Growth Rate'] = gdp_df['GDP'].pct_change() * 100  # Calculate % change

# Save the processed data
processed_file_path = "data//processed//FRED_GDP_processed.csv"
gdp_df.to_csv(processed_file_path, index=False)

print(f"Processed data saved to {processed_file_path}")

# Print first few rows of the processed dataset for verification
print(gdp_df.head(10))