import sys
import json
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from together import Together
import requests
from requests.auth import HTTPBasicAuth

# ----------------------------
# 1. CONFIGURATION
# ----------------------------
client = Together(api_key="7c250b03ffca377edb3b61d3d11bea4c1f2ab4c7f156851e8b6ff5844916f719")

opensearch_host = 'search-vector-db-muujojc433yrk6olm7ccipzsdi.us-east-1.es.amazonaws.com'
index_name = 'rag-index-embeddings'
vector_field = 'embedding'
text_field = 'chunk_text'

# OpenSearch Basic Auth Credentials
master_username = 'af978'
master_password = 'VirtEcon2!'
auth = HTTPBasicAuth(master_username, master_password)

embedding_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# ----------------------------
# 2. PIPELINE FUNCTIONS
# ----------------------------
def embed_query_locally(query: str) -> list:
    embedding = embedding_model.encode(query, normalize_embeddings=True)
    return embedding.tolist()

def search_opensearch_knn(embedding: list, k: int) -> list:
    search_url = f"https://{opensearch_host}/{index_name}/_search"
    query_body = {
        "size": k,
        "query": {
            "knn": {vector_field: {"vector": embedding, "k": k}}
        },
        "_source": [text_field]
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(search_url, auth=auth, headers=headers, data=json.dumps(query_body))
    if response.status_code != 200:
        raise Exception(f"OpenSearch query failed: {response.status_code} {response.text}")
    hits = response.json().get('hits', {}).get('hits', [])
    return [hit['_source'][text_field] for hit in hits]

def deduplicate_chunks(chunks: list) -> list:
    seen = set()
    unique = []
    for chunk in chunks:
        key = chunk.strip().lower()
        if key not in seen:
            seen.add(key)
            unique.append(chunk)
    return unique

def trim_context_to_token_limit(chunks, max_tokens=3000):
    trimmed, token_count = [], 0
    for chunk in chunks:
        tokens = len(tokenizer.encode(chunk))
        if token_count + tokens <= max_tokens:
            trimmed.append(chunk)
            token_count += tokens
        else:
            break
    return trimmed

def build_prompt(query, context_chunks):
    context_text = "\n\n".join(context_chunks)
    return f"""You are a helpful and knowledgeable AI assistant specialized in economics and financial analysis. Use the context below to answer the question accurately and concisely.

For numeric formatting, if a number is between 0 and 1 and originally shown with a percentage sign (e.g., 0.09678%), keep the percent sign in the output. If a number is 1 or higher and shown as a percentage, treat it as a raw number without including a percent sign.

Use economic indicators, historical patterns, and trends in the data (such as GDP signals, recession flags, interest rates, and other macroeconomic markers) to form your analysis and predictions. If direct data is missing, rely on logical inference using related information.

When dealing with population data, interpret numbers in thousands and present all final population values in millions, rounded to two decimal places. For example, if a population is 310232.863, your output should state it as 310.23 million.

Do not explain formatting rules in your output. Focus solely on providing a clear, relevant, and insightful response.

Context:
{context_text}

Question: {query}
Answer:"""

def call_together_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def rag_query_pipeline(user_query: str):
    k = 25  # Fixed number of chunks
    embedding = embed_query_locally(user_query)
    chunks = search_opensearch_knn(embedding, k)
    chunks = deduplicate_chunks(chunks)
    chunks = trim_context_to_token_limit(chunks, max_tokens=3000)
    prompt = build_prompt(user_query, chunks)
    answer = call_together_llm(prompt)
    return answer

# ----------------------------
# 3. MAIN ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No question provided."}))
        sys.exit(1)

    user_query = sys.argv[1]
    try:
        result = rag_query_pipeline(user_query)
        print(json.dumps({"answer": result}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
