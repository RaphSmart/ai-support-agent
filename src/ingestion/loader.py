from pypdf import PdfReader
import os


# document ingestion 

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    

def load_pdf(path):
    reader = PdfReader(path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def chunk_text(text, chunk_size=200):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))

    return chunks


def load_documents(folder="data"):

    all_chunks = []

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            text = load_text(path)

        elif file.endswith(".pdf"):
            text = load_pdf(path)

        else:
            continue

        chunks = chunk_text(text)

        all_chunks.extend(chunks)

    return all_chunks

