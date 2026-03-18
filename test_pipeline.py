from pathlib import Path
from src.core.pipeline import SupportAgentPipeline

MODEL_PATH = Path("models/phi-2.gguf")

pipeline = SupportAgentPipeline(model_path=MODEL_PATH)


# Igest document
pipeline.ingest([
    "Customers can request refunds within 30 days."
])

# ask question
answer1 = pipeline.query("What is refund policy?")
print("Answer 1:", answer1)

# Follow-up question (memory test)
answer2 = pipeline.query("How long does it last?")
print("Answer 2:", answer2)
