import pyfredapi as pf
import time

def get_all_subcategories(category_id, api_key):
    """
    Recursively fetch all subcategories from the given category_id.
    """
    subcategories = []
    children = pf.get_category_children(category_id=category_id, api_key=api_key).get('categories', [])
    
    if not children:  # If no children, return this category as lowest level
        return [category_id]
    
    for child in children:
        subcategories.extend(get_all_subcategories(child['id'], api_key))
        time.sleep(0.5)  # Avoid hitting API limits
    
    return subcategories

# Replace with your FRED API key
API_KEY = "8bc4e28ada12118ea9c031306e66482c"

# Root category for Money, Banking, & Finance
root_category_id = 32991 # 10, 32992, 1, 32455

# 32991   'Money, Banking, & Finance'
# 10      'Population, Employment, & Labor Markets'
# 32992   'National Accounts' 
# 1       'Production & Business Activity'
# 32455   'Prices'
# 32263   'International Data'
# 3008    'U.S. Regional Data'
# 33060   'Academic Data'

# Get all lowest-level categories under Money, Banking, & Finance
lowest_level_categories = get_all_subcategories(root_category_id, API_KEY)

# Print the list of all lowest-level categories
print("Lowest-level categories:", lowest_level_categories)
print(len(lowest_level_categories))
