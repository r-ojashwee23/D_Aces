import pandas as pd
from fuzzywuzzy import process

# Read CSV files
classification_df = pd.read_csv("Dataset_Classification.csv")
categories_df = pd.read_csv("Categories_Description.csv")

# Preprocess data
classification_df['title'] = classification_df['title'].str.lower().str.strip()
categories_df['name'] = categories_df['name'].str.lower().str.strip()

# Function to find category for a title
def find_category(title):
    category_names = categories_df['name']
    matched_name, score, index = process.extractOne(title, category_names)
    
    # Set a threshold score for matching
    if score >= 80:  # You can adjust the threshold as needed
        return matched_name
    else:
        return "Unknown"

# Add a new 'category' column to the classification dataframe
classification_df['category'] = classification_df['title'].apply(find_category)

# Print the updated classification dataframe
print(classification_df)

# Save the updated classification dataframe to a new CSV file
classification_df.to_csv("Updated_Dataset_Classification.csv", index=False)
