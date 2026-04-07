from llama_cpp import Llama
from pathlib import Path
import urllib.request


MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODEL_DIR / "tinyllama.gguf"


def download_model():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    if MODEL_PATH.exists():
        print("Model already exists.")
        return
    
    print("Downloading TinyLlama model (first run only)...")

    req = urllib.request.Request(
        MODEL_URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req) as response, open(MODEL_PATH, "wb") as f:
        
        total_size = int(response.getheader("Content-Length", 0))
        downloaded = 0
        chunk_size = 8192

        while True:
            chunk = response.read(chunk_size)
            if not chunk:
                break

            f.write(chunk)
            downloaded += len(chunk)

            # display download progress
            percent = downloaded * 100 // total_size if total_size else 0
            print(f"\rDownloading... {percent}%", end="")

    print("\nModel downloaded.")


class LocalLLM:

    def __init__(self, model_path=None):

        download_model()

        print("Loading LLM...")

        self.llm = Llama(
            model_path=str(MODEL_PATH),
            n_ctx=2048,
            n_threads=4,
            verbose=False
        )

        print("LLM loaded.")

    def generate(self, prompt: str) -> str:

        output = self.llm(
            prompt,
            max_tokens=150,
            temperature=0.3,
            top_p=0.9,
            stop=["User:", "Assistant:"]
        )

        return output["choices"][0]["text"].strip()


if __name__ == "__main__":

    llm = LocalLLM()

    response = llm.generate(
        "User: What is artificial intelligence?\nAssistant:"
    )

    print(response)




# from llama_cpp import Llama
# from pathlib import Path
# import urllib.request



# MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-GGUF/resolve/main/tinyllama-1.1b-chat.Q4_K_M.gguf"


# PROJECT_ROOT = Path(__file__).resolve().parents[2]
# MODEL_DIR = PROJECT_ROOT / "models"
# MODEL_PATH = MODEL_DIR / "tinyllama.gguf"

# def download_model():
#     MODEL_DIR.mkdir(parents=True, exist_ok=True)

#     if not MODEL_PATH.exists():
#         print("Downloading tinyllama model... (first run only)")
#         urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
#         print("Model downloaded.")


# class LocalLLM:

#     def __init__(self, model_path=None):

#         download_model()
#         # print("Loading LLM...")

#         self.llm = Llama(
#             model_path=MODEL_PATH,
#             n_ctx=2048,
#             n_threads=4,
#             verbose=False
#         )

#         print("LLM loaded.")

#     def generate(self, prompt: str) -> str:

#         output = self.llm(
#             prompt,
#             max_tokens=80,        # reduced for concise answers
#             temperature=0.1,       # lower = more factual, less rambling
#             stop=["User:", "Assistant:"]
#         )

#         return output["choices"][0]["text"].strip()