import requests
import pandas as pd

# Read the datasets
classification_data = pd.read_csv('Dataset_Classification.csv')
categories_data = pd.read_csv('Categories_Description.csv')

# API endpoint
url = "https://api.meaningcloud.com/class-2.0"

# Your MeaningCloud API key
api_key = "7ed73d18f6626604b800815aa305f996"

# Iterate through each row in the classification dataset
for index, row in classification_data.iterrows():
    content = row['content']
    
    # Construct the payload
    payload = {
        'key': api_key,
        'txt': content,
        'model': 'SocialMedia_en',
        'of': 'json'
    }
    
    # Make the API request
    response = requests.post(url, data=payload)
    result = response.json()
    
    # Extract the categories
    if 'category_list' in result:
        categories = [category['label'] for category in result['category_list']]
    else:
        categories = []
    
    # Update the corresponding row in the classification dataset
    classification_data.at[index, 'categories'] = ', '.join(categories)

# Save the updated classification dataset
classification_data.to_csv('Updated_Dataset_Classification.csv', index=False)