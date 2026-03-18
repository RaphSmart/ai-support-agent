from src.embeddings.embedder import Embedder
from src.vectorstore.vector_store import VectorStore

embedder = Embedder()

texts = [
    "Refund policy is 30 days",
    "Shipping takes 5 days",
    "Support email is support@company.com"
]

embeddings = embedder.embed(texts)

dimension = len(embeddings[0])

store = VectorStore(dimension)

store.add(embeddings, texts)

query = "How long is refund?"

query_embedding = embedder.embed([query])[0]

results = store.search(query_embedding)

print(results)