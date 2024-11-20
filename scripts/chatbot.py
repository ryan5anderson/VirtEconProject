from preprocess import preprocess_data
from embeddings import create_embeddings, build_faiss_index
from query_model import query_model
import os

if __name__ == "__main__":
    # Ensure data has been processed
    if not os.path.exists("data/processed/documents.txt"):
        documents = preprocess_data()
        embeddings = create_embeddings(documents)
        build_faiss_index(embeddings)

    # Chatbot interaction
    while True:
        user_query = input("Ask your question about GDP or historical events (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        response = query_model(
            query=user_query,
            faiss_index_path="data/processed/faiss_index",
            documents_path="data/processed/documents.txt",
            embeddings_path="data/processed/doc_embeddings.npy"
        )
        print("\nChatbot Response:", response)