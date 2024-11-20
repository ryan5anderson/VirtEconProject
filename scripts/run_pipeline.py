import os

os.system("python scripts//fetch_gdp_data.py")
os.system("python scripts//process_gdp_data.py")
os.system("python scripts//historical_events.py")
os.system("python scripts//integrate_metadata.py")
print("Data pipeline completed.")