import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

def fetch_historical_events():
    # URL for the Wikipedia page
    url = "https://en.wikipedia.org/wiki/List_of_recessions_in_the_United_States"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Locate the specific section header "Great Depression onward (1929–present)"
    section_header = soup.find("span", {"id": "Great_Depression_onward_.281929.E2.80.93present.29"})
    if not section_header:
        print("Section not found!")
        return
    
    # Find the next table after the section header
    table = section_header.find_next("table", {"class": "wikitable"})
    if not table:
        print("Table not found in the section!")
        return

    # Parse the table
    rows = table.find_all("tr")  # All rows in the table
    headers = [th.text.strip() for th in rows[0].find_all("th")]  # Extract column names

    # Ensure the headers match the expected structure
    print(f"Table Headers: {headers}")

    # Extract data from the table rows
    events = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all("td")
        if len(cells) >= 7:  # Ensure there are enough columns
            name = cells[0].text.strip()               # Name of the event
            period_range = cells[1].text.strip()       # Period Range
            characteristics = cells[6].text.strip()   # Characteristics (description)
            
            cleaned_range = re.sub(r"\[.*?\]", "", period_range)  # Remove brackets and contents
            cleaned_char = re.sub(r"\[.*?\]", "", characteristics)

            # Parse start and end years from the period range
            if "–" in cleaned_range:  # Handles ranges like "1946–1949"
                try:
                    start_year, end_year = map(str, cleaned_range.split("–"))
                except ValueError:
                    print("Value Error")
                    continue
            else:  # Handles single years like "1945"
                try:
                    start_year = int(cleaned_range.split(" ")[0])
                    end_year = start_year
                except ValueError:
                    continue
              # Function to extract year from strings like "February 2001"
            def extract_year(date_str):
                match = re.search(r"\b(19|20)\d{2}\b", date_str)  # Match years like 1920-2099
                return int(match.group()) if match else None

            # Extract Start and End Years
            start_year = extract_year(period_range.split("–")[0])
            end_year = extract_year(period_range.split("–")[-1])

            # Include only events starting in 1946 or later
            events.append({
                "Name": name,
                "Start Year": start_year,
                "End Year": end_year,
                "Description": cleaned_char
            })

    # Convert to DataFrame
    print(events)
    events_df = pd.DataFrame(events)
    

    # Save to CSV
    file_path = "data/processed/historical_events.csv"
    events_df.to_csv(file_path, index=False)
    print(f"Historical events saved to {file_path}")

# Run the function
fetch_historical_events()