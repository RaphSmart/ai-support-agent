from fastapi import FastAPI
from pydantic import BaseModel
import uuid

from src.core.agent_manager import AgentManager


app = FastAPI()

# Initialize once at startup
manager = AgentManager("models/tinyllama.gguf")


class ChatRequest(BaseModel):
    question: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    session_id: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    session_id = request.session_id or str(uuid.uuid4())

    agent = manager.get_agent(session_id)
    answer = agent.answer(request.question)

    return ChatResponse(
        answer=answer,
        session_id=session_id
    )


# What This Does

# - Each user gets their own agent instance

# - Each session has isolated memory

# - Conversations do not leak across users

# - API becomes multi-user ready