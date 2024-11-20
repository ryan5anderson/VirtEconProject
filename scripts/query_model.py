from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def query_model(query, faiss_index_path, documents_path, embeddings_path):
    # Load FAISS index
    index = faiss.read_index(faiss_index_path)

    # Load documents and embeddings
    with open(documents_path, "r") as f:
        documents = f.read().splitlines()
    embeddings = np.load(embeddings_path)

    # Load a Hugging Face LLM (e.g., Falcon, BLOOM, GPT-NeoX)
    llm = pipeline("text-generation", model="unsloth/Llama-3.2-3B-Instruct", device=-1)

    # Generate embedding for the query
    query_embedding = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2').encode([query])

    # Search for the top 3 most relevant documents
    distances, indices = index.search(query_embedding, k=3)
    retrieved_docs = [documents[i] for i in indices[0]]

    # Combine retrieved documents into a context
    context = "\n".join(retrieved_docs)

    # Generate a response using the context
    input_text = f"Context:\n{context}\n\nQuery:\n{query}\n\nAnswer:"
    response = llm(input_text, max_new_tokens=150, num_return_sequences=1)

    return response[0]['generated_text']
