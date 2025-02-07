import pyfredapi as pf
import time

# Replace with your FRED API key
API_KEY = "8bc4e28ada12118ea9c031306e66482c"

# List of category IDs
category_ids = [34009, 33058, 51] # 121, 120, 32348, 33059, 
                # 34005, 34007, 32298, 118, 33056, 33446, 32299, 
                # 32995, 33055, 114, 33057, 117, 33491, 34003, 
                # 116, 115, 82, 94, 95, 32219, 105, 287, 286, 
                # 285, 284, 283, 282, 281, 280, 279, 278, 277, 
                # 274, 273, 272, 271, 276, 275, 270, 269, 268, 
                # 266, 265, 264, 263, 262, 261, 260, 259, 258, 
                # 257, 267, 254, 191, 192, 124, 123, 25, 29, 96, 
                # 28, 30, 26, 32242, 122, 32215, 32218, 32413, 33119, 
                # 32457, 32255, 32425, 34078, 33078, 33079, 33080, 33081, 
                # 33082, 93, 84, 85, 86, 87, 88, 89, 90, 91, 92, 101, 32440, 
                # 33121, 72, 65, 66, 67, 68, 69, 70, 71, 33445, 32439, 99, 
                # 34111, 32239, 32996, 32407, 32408, 32409, 32410, 32411, 
                # 32412, 33439, 32362, 32369, 32364, 32367, 32368, 32366, 
                # 32365, 32363, 32371, 32375, 32372, 32373, 32374, 32376, 
                # 32377, 32378, 32380, 32381, 32382, 32383, 32384, 32385, 
                # 32386, 32387, 32389, 32390, 32391, 32392, 32393, 32394, 
                # 32395, 32396, 32398, 32399, 32400, 32401, 32402, 32403, 
                # 32404, 32405, 33440, 32145]

# Dictionary to store all series data
all_series_data = {}

# Loop through each category ID and fetch series data
for category_id in category_ids:
    series_data = pf.get_category_series(category_id=category_id, api_key=API_KEY)

    # Merge the results into all_series_data
    all_series_data.update(series_data)

    # Optional: Add a small delay to avoid rate limits
    time.sleep(0.5)  

# Print all the collected series IDs
print("Collected Series IDs:", all_series_data)