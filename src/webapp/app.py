import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/chat")

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

    # Call API with loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={
                        "question": prompt,
                        "session_id": st.session_state.session_id
                    },
                    timeout=60  # prevents hanging forever
                )

                # ✅ Check HTTP status FIRST
                if response.status_code != 200:
                    st.error(f"API Error: {response.status_code}")
                    st.text(response.text)
                    answer = "Something went wrong on the server."
                else:
                    # ✅ Safely parse JSON
                    try:
                        data = response.json()
                        st.session_state.session_id = data.get("session_id")
                        answer = data.get("answer", "No answer returned.")
                    except Exception:
                        st.error("Invalid JSON response from API")
                        st.text(response.text)
                        answer = "Invalid response from server."

            except requests.exceptions.RequestException as e:
                st.error("Connection error to API")
                st.text(str(e))
                answer = "Could not reach the backend."

        # Show assistant message
        st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})