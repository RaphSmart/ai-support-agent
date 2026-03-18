from src.embeddings.embedder import Embedder

embedder = Embedder()

texts = [
    "Refund policy",
    "Shipping policy"
]

embeddings = embedder.embed(texts)

print("Shape:", embeddings.shape)