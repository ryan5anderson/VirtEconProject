import pandas as pd

def preprocess_data():
    # Load the enriched GDP data
    gdp_df = pd.read_csv("data/processed/GDP_enriched.csv")

    # Combine relevant columns into a single text field for embeddings
    gdp_df['Combined Text'] = gdp_df.apply(
        lambda row: f"Year: {row['Year']}, Quarter: {row['Quarter']}, GDP: {row['GDP']}, "
                    f"GDP Growth Rate: {row['GDP Growth Rate']}, Event Name: {row['Event Name']}, "
                    f"Event Description: {row['Event Description']}",
        axis=1
    )

    # Return the combined text
    return gdp_df['Combined Text'].tolist()