# 📄 AI Support Agent (Local RAG Chatbot)

This is a local AI support chatbot that answers questions using company documentation.

This project implements a Retrieval-Augmented Generation (RAG) system using a local LLM (TinyLlama), semantic search with SentenceTransformers, and FAISS for vector similarity.

The system can ingest PDF or TXT documents and answer questions based on knowledge provided.


# ✨ Features
• Local LLM (TinyLlama via llama.cpp)
• Automatic model download
• Document ingestion (PDF + TXT)
• Semantic embeddings using SentenceTransformers
• FAISS vector database
• Retrieval-Augumented Generation (RAG)
• Chat history memory
• FastAPI backend API
• Streamlit UI
• Docker
• Persistent vector database


🧠 Architecture
User Question
     │
     ▼
SentenceTransformer Embedding
     │
     ▼
FAISS Vector Search
     │
     ▼
Relevant Document Chunks
     │
     ▼
Prompt Construction
     │
     ▼
TinyLlama Local LLM
     │
     ▼
AI Generated Answer


# ⚙️ Installation

Clone repository
```bash
git clone <https://github.com/RaphSmart/ai-support-agent>
cd ai-support-agent
```

# Install dependencies:
```bash
pip install -r requirements.txt
```

# Run backend - FasAPI
Start the FastAPI server:
```bash
uvicorn api.main:app --reload
```
API runs on the port:
```bash
http://localhost:8000
```

# Run UI
Launch streamlit interface:
```bash
streamlit run ui/app.py
```
Opens in browser
```bash
http://localhost:8501
```

# If model is not found
download from:
```bash
https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
```
Download file:
tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

📂 Place the downloaded file in models folder:
models/tinyllama.gguf
(Create the folder if it doesn't already exist)

# If data folder is not found
Create the folder:
data/

# 📚 Add Knowledge
Place documents in the data folder
Supported formats:
    • .txt
    • .pdf

The system automatically
    • loads documents
    • splits into chunks
    • generates embeddings
    • stores them in FAISS

# ⛴️🐳 Docker with the app

docker build --no-cache -t smart_rag . 

# Service       Port
FastAPI API	    8000
Streamlit UI	8501

# docker-compose with the app
```bash
docker-compose up
```

# 🙋🏻‍♂️ Example Questions 
What is your refund policy?

How can I contact support?

What services does the company offer?


# 💻 Tech Stack
Backend
 • FastAPI
 • Python

AI/ML
 • TinyLlama (GGUF)
 • llama-cpp-python
 • SentenceTransformers
 • FAISS

Frontend
 • Streamlit

Infrastructure
 • Docker
 • Docker Compose


# 🚀 Future Improvements
Planned upgrades:
• Streaming LLM responses
• Web document ingestion
• Support for multiple models (Mistral, Phi, Llama 3)
• Vector database alternatives (Chroma / Qdrant)
• Authentication layer
• Deployment to cloud infrastructure


# 🎯 Use Cases
• Customer support automation
• Internal company knowledge assistant
• FAQ chatbot
• Product documentation assistant
• Developer documentation helper


# 👨‍💻 Author
Built this project as a portfolio AI engineering project demonstrating:
• Retrieval-Augumented Generation
• Local LLM deployment
• Vector search pipelines
• AI system architecture
• Full-stack AI application development