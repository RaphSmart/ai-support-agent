from src.embeddings.embedder import Embedder
from src.vectorstore.faiss_store import VectorStore
from src.llm.local_llm import LocalLLM
from src.ingestion.loader import load_documents


class SupportAgentPipeline:

    def __init__(self, model_path: str):

        print("Initializing Support Agent...")

        self.embedder = Embedder()

        test_embedding = self.embedder.embed(["test"])[0]
        dimension = len(test_embedding)

        self.vectorstore = VectorStore(dimension)
        self.llm = LocalLLM(model_path)

        # Add short-term conversational memory so the agent remembers previous messages during a session.
        self.memory = []  

        # Auto ingest if empty
        if len(self.vectorstore.texts) == 0:
            print("No existing knowledge base found. Ingesting data...")
            self.ingest_folder("data")
            

        print("Support Agent ready.")


    # Ingestion plugin (update after modifying loader.py)
    def ingest_folder(self, folder="data"):

        texts = load_documents(folder)

        if not texts:
            print("No documents found to ingest.")
            return 

        print(f"Ingesting {len(texts)} chunks...")

        self.add_knowledge(texts)
    
    # End of ingestion plugin (update after modifying loader.py)


    def add_knowledge(self, texts):

        embeddings = self.embedder.embed(texts)
        self.vectorstore.add(texts, embeddings)


    def answer(self, question: str, k: int = 3):

        # Store user message in memory
        self.memory.append(f"User: {question}")

        question_embedding = self.embedder.embed([question])[0]
        results = self.vectorstore.search(question_embedding, k=k)

        # Hendle empty context
        if not results:
            context = "No relevant knowledfe found."
        else:
            context = "\n".join(results)

        conversation_history = "\n".join(self.memory[-3:])  # last 4 messages only

        prompt = f"""<|system|>
You are a professional AI support agent.

Rules:
- Answer ONLY using the provided knowledge
- If the answer is not in the knowledge, say "I don't know"
- Be concise and helpful

<|context|>
{context}

<|conversation|>
{conversation_history}

<|user|>
{question}

<|assistant|>
"""

        answer = self.llm.generate(prompt)

        # Store assistant response
        self.memory.append(f"Assistant: {answer}")

        return answer
