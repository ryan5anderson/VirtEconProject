from transformers import pipeline
import pandas as pd

#Load the model
qapipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

#Load your data
gdp_data = pd.read_csv("data//raw//GDP.csv")

#Prepare the rawdata with clear chunking
chunks = []
chunk_size = 5  # Combine 5 rows into one chunk for context
for i in range(0, len(gdp_data), chunk_size):
    chunk = " ".join([f"{row['DATE']}: {row['GDP']} billion dollars" for _, row in gdp_data.iloc[i:i+chunk_size].iterrows()])
    chunks.append(chunk)

#Example question
question = "What was the GDP in 2001-04-01?"

#List to store all results
results = []

#Get the answer from each chunk
for chunk in chunks:
    print("CHUNK######## ", chunk)
    result = qapipeline(question=question, context=chunk)
    results.append(result)
    print("result########### ", result)

#Sort results by score in descending order
sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)

#Get top 10 results
top_10_results = sorted_results[:10]

#Print top 10 results
for i, res in enumerate(top_10_results, start=1):
    print(f"Top {i}: Answer = {res['answer']}, Score = {res['score']}")