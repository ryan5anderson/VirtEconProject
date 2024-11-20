import pandas as pd

def integrate_metadata():
    # Load GDP data
    gdp_df = pd.read_csv("data/processed/FRED_GDP_processed.csv")

    # Load historical events
    events_df = pd.read_csv("data/processed/historical_events.csv")

    # Ensure the Event Name and Description columns exist in the GDP DataFrame
    gdp_df['Event Name'] = None
    gdp_df['Event Description'] = None

    # Iterate over historical events
    for _, event in events_df.iterrows():
        # Extract event details
        start_year = event['Start Year']
        end_year = event['End Year']
        name = event['Name']
        description = event['Description']

        # Update the Event Name and Description columns for GDP rows within the date range
        gdp_df.loc[
            (gdp_df['Year'] >= start_year) & (gdp_df['Year'] <= end_year),
            ['Event Name', 'Event Description']
        ] = [name, description]

    # Save enriched data
    enriched_file_path = "data/processed/GDP_enriched.csv"
    gdp_df.to_csv(enriched_file_path, index=False)
    print(f"Enriched GDP data saved to {enriched_file_path}")

# Run the function
integrate_metadata()
