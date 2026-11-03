# 🏋️ RAG-Based Gym Information Chatbot

This project is a FastAPI-based chatbot that uses Retrieval-Augmented Generation (RAG) to answer **gym-related questions**. It retrieves relevant text chunks from a local knowledge base and uses an LLM API (Fireworks) to generate contextual answers.


https://github.com/user-attachments/assets/349e5d31-1836-458a-83d4-92fe122c5eb1


---

## 🚀 Features

- 🔹 **FastAPI backend** with REST endpoints
- 🔹 **ChromaDB** for storing and retrieving embedded gym data
- 🔹 **SentenceTransformer** for vector embeddings
- 🔹 **Fireworks LLM API** for text generation
- 🔹 **Streamlit UI** for user interaction
- 🔹 Strict filtering to answer only gym/fitness/exercise-related questions

---

## 🧾 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
