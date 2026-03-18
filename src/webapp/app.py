import streamlit as st
import requests


import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/chat")

# API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Support Agent", page_icon="🤖")

st.title("🤖 AI Support Agent")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
if prompt := st.chat_input("Ask a question..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    
    # Send request to API
    response = requests.post(
        API_URL,
        json={
            "question": prompt,
            "session_id": st.session_state.session_id
        }
    )

    data = response.json()

    st.session_state.session_id = data["session_id"]

    answer = data["answer"]


    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)