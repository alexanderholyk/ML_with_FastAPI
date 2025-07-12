# train_model.py
# by Alex Holyk

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

try:
    df = pd.read_csv('IMDB Dataset.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("File not found. Please ensure 'IMDB Dataset.csv' is in the current directory.")

# Split the dataset into features (X) and labels (y)
X = df['review']
y = df['sentiment']

# Create a pipeline that first transforms the text data using TF-IDF and then applies a Naive Bayes classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the pipeline on entire dataset (not separating into train/test)
pipeline.fit(X, y)

# Save the trained model to a file
joblib.dump(pipeline, 'sentiment_model.pkl')
print("Model trained and saved as 'sentiment_model.pkl'.")