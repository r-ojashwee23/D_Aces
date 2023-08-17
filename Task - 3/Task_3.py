import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load and preprocess the datasets
classification_data = pd.read_csv('Dataset_Classification.csv')
description_data = pd.read_csv('Categories_Description.csv')

# Assuming classification_data has 'content' and 'category' columns
X_train = classification_data['content']
y_train = classification_data['title']

# Assuming description_data has 'description' and 'name' columns
X_test = description_data['description']
names = description_data['name']

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)

# Classify descriptions and create a new dataframe
classified_categories = classifier.predict(X_test_vec)
classified_df = pd.DataFrame({'content': X_test, 'description': classified_categories, 'name': names})

# Save the final classified dataset to a CSV file
classified_df.to_csv('Final_Classified_Dataset.csv', index=False)
