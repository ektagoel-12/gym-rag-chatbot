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

Create a `.env` file in the project root:

```env
FIREWORKS_API_KEY=your_key_here
```

---

## ▶️ Run it

1. Build the vector index from `data/gym_data.txt`:

```bash
python -m app.data_loader
```

2. Start the API (the Streamlit UI expects port 8000):

```bash
uvicorn app.main:app --port 8000
```

3. In a second terminal, start the UI:

```bash
streamlit run streamlit_app.py
```

Streamlit also needs `streamlit` and `requests` installed (they are not in `requirements.txt` yet):

```bash
pip install streamlit requests
```

## 🔌 API

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Health check |
| `/chat` | POST | Body `{"query": "..."}`; returns the answer and the source chunks |
| `/reset` | POST | Placeholder, there is no session state |

## 🗂️ Project structure

```
app/main.py          FastAPI app and endpoints
app/data_loader.py   Splits data/gym_data.txt into chunks and stores embeddings
app/rag.py           Retrieval (ChromaDB + all-MiniLM-L6-v2) and Fireworks generation
streamlit_app.py     Chat UI
data/gym_data.txt    Knowledge base
test_chat.py         Quick chat test script
```

## 🧠 How it works

1. Gym articles in `data/gym_data.txt` are split into chunks and embedded with `all-MiniLM-L6-v2`.
2. The embeddings are stored in a local ChromaDB (`.chromadb/`).
3. For each question, the top 3 chunks are retrieved and sent to a Fireworks-hosted Llama 4 model.
4. The prompt tells the model to answer only from that context and to refuse non-gym questions.
