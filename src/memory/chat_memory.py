# chat memory
class ChatMemory:
    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.messages = []

    def add_user_message(self, message: str):
        self.messages.append({
            "role": "user",
            "content": message
        })
        self._trim()

    def add_ai_message(self, message: str):
        self.messages.append({
            "role": "assistant",
            "content": message
        })
        self._trim()

    def get_messages(self):
        return self.messages
    
    def clear(self):
        self.messages = []

    def _trim(self):
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]