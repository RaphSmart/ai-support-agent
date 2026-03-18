from src.core.pipeline import SupportAgentPipeline

agent = SupportAgentPipeline("models/tinyllama.gguf")

# Add the knowledge
agent.add_knowledge([
    "Refunds are allowed within 30 days.",
    "Shipping takes 3 to 5 business days.",
    "You can reset your password using the reset link."
])

# Ask question
response = agent.answer("Can I get a refund after purchase?")

print("\nAI Answer:")
print(response)
