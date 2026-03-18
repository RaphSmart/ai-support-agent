# Updated code, first/version one code below

import faiss
import numpy as np
import pickle
import os


class VectorStore:
    def __init__(self, dimension: int, index_path="vector.index", doc_path="docs.pkl"):
        
        print("Initializing FAISS vector store...")

        self.dimension = dimension
        self.index_path = index_path
        self.doc_path = doc_path

        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

        # Try loading existing index
        if os.path.exists(index_path):
            self.load()

        print("FAISS ready.")

    
    def add(self, texts, embeddings):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)
        self.texts.extend(texts)

        print(f"{len(texts)} documents added.")

        self.save()


    def search(self, query_embedding, k=3):

        if self.index.ntotal == 0:
            return []
        
        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for idx in indices[0]:
            if 0 <= idx < len(self.texts):
                results.append(self.texts[idx])

        return results
    
    def save(self):

        faiss.write_index(self.index, self.index_path)

        with open(self.doc_path, "wb") as f:
            pickle.dump(self.texts, f)

        print("Vector store saved.")


    def load(self):

        self.index = faiss.read_index(self.index_path)

        with open(self.doc_path, "rb") as f:
            self.texts = pickle.load(f)

        print("Vectore store loaded.")






## ----"Original Code"----

# import faiss
# import numpy as np



# class VectorStore:
#     def __init__(self, dimension: int):

#         print("Initializing FAISS vector store...")

#         self.dimension = dimension

#         # FAISS index (L2 distance)
#         self.index = faiss.IndexFlatL2(dimension)

#         self.texts = []

#         print("FAISS ready.")

#     def add(self, texts, embeddings):

#         embeddings = np.array(embeddings).astype("float32")
#         self.index.add(embeddings)
#         self.texts.extend(texts)

#         print(f"{len(texts)} documents added.")

#     def search(self, query_embedding, k=3):

#         if self.index.ntotal == 0:
#             return []
        
#         query_embedding = np.array([query_embedding]).astype("float32")

#         distances, indices = self.index.search(query_embedding, k)

#         results = []

#         for idx in indices[0]:
#             if 0<= idx < len(self.texts):
#                 results.append(self.texts[idx])

#         return results 