from src.memory.chat_memory import ChatMemory

memory = ChatMemory()


memory.add_user_message("Hello")
memory.add_ai_message("Hi, how can I help you?")

memory.add_user_message("What is refund policy?")

print(memory.get_messages())