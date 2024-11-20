from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Load the model
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Load your data
gdp_data = pd.read_csv("data//raw//GDP.csv")

# Prepare the data as text for similarity checks
gdp_data['text'] = gdp_data.apply(lambda row: f"{row['DATE']}: {row['GDP']} billion dollars", axis=1)

# Example question
question = "What was the GDP in 1949-01-01?"

# Step 1: Perform similarity check
# Create a TF-IDF matrix for the question and GDP data
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([question] + gdp_data['text'].tolist())

# Calculate cosine similarity between the question and each row
similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Add similarity scores to the dataframe
gdp_data['similarity'] = similarities

# Sort data by similarity scores in descending order
gdp_data_sorted = gdp_data.sort_values(by='similarity', ascending=False)

# Select the top 3 most similar rows for context
top_context_rows = gdp_data_sorted.head(5)['text'].tolist()
context = " ".join(top_context_rows)

# Step 2: Pass the best context into the QA model
result = qa_pipeline(question=question, context=context)

# Print the final result
print(f"Question: {question}")
print(f"Answer: {result['answer']}")
print(f"Score: {result['score']}")
print(f"Context used: {context}")