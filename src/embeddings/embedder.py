from sentence_transformers import SentenceTransformer
import numpy as np


class Embedder:

    # Converts text into vector embeddings."
    def __init__(self, model_name ="sentence-transformers/all-MiniLM-L6-v2"):
        
        print("Loading embedding model...")

        self.model = SentenceTransformer(model_name)

        print("Embedding model loaded.")

    def embed(self, texts: list[str]) -> np.ndarray:

        # Convert list of texts into embeddings.
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings
    