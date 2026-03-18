from src.llm.local_llm import LocalLLM

llm = LocalLLM("models/tinyllama.gguf")

prompt = """
You are a helpful support agent.

Question: What is your refund policy?

Answer:
"""

response = llm.generate(prompt)

print(response)