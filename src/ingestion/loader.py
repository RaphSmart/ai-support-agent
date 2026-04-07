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

    # Latest update, if folder does not exist, create it and continue safely without crashing
    if not os.path.exists(folder):
        print(f" '{folder}' folder not found. Creating it...")
        os.makedirs(folder, exist_ok=True)
        return []

    # End of latest update, 

    all_chunks = []

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            text = load_text(path)

        elif file.endswith(".pdf"):
            text = load_pdf(path)

        else:
            continue

        # Added for folder not exist
        if not text.strip():
            continue
        # End of code

        chunks = chunk_text(text)

        all_chunks.extend(chunks)

    if not all_chunks:
        print("No documents found in data folder.")

    return all_chunks

