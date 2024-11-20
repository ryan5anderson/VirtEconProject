from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def create_embeddings(documents):
    # Load a Hugging Face Sentence Transformer model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Generate embeddings for the documents
    embeddings = model.encode(documents)

    # Save embeddings and documents for later use
    np.save("data/processed/doc_embeddings.npy", embeddings)
    with open("data/processed/documents.txt", "w") as f:
        f.writelines("\n".join(documents))

    return embeddings

def build_faiss_index(embeddings):
    # Initialize FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to the index
    index.add(embeddings)

    # Save the index
    faiss.write_index(index, "data/processed/faiss_index")
    print("FAISS index saved.")