from src.core.pipeline import SupportAgentPipeline


class AgentManager:

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.sessions = {}

    def get_agent(self, session_id: str):

        if session_id not in self.sessions:
            self.sessions[session_id] = SupportAgentPipeline(self.model_path)
        
        return self.sessions[session_id]