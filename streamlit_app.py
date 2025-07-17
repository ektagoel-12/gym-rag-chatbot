import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🏋️‍♀️ Gym Info Chatbot")

# Chat functionality
query = st.text_input("Ask a gym-related question:")
if st.button("Send"):
    if query.strip():
        with st.spinner("Getting answer..."):
            response = requests.post(f"{API_URL}/chat", json={"query": query})
            if response.status_code == 200:
                st.success(response.json()["response"])
            else:
                st.error("Failed to get response from server.")
    else:
        st.warning("Please enter a question.")

# Divider
st.markdown("---")

# ✅ Health check
if st.button("Check Server Health"):
    try:
        response = requests.get(f"{API_URL}/health")
        if response.status_code == 200:
            st.success("✅ Server is healthy: " + response.text)
        else:
            st.error("❌ Health check failed.")
    except Exception as e:
        st.error(f"Exception: {e}")

# ✅ Reset endpoint (if implemented)
if st.button("Reset Conversation"):
    try:
        response = requests.post(f"{API_URL}/reset")
        if response.status_code == 200:
            st.success("🧹 Conversation history reset.")
        else:
            st.error("❌ Failed to reset.")
    except Exception as e:
        st.error(f"Exception: {e}")
