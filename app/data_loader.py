import os
from sentence_transformers import SentenceTransformer
import chromadb
import re

DATA_FILE = "data/gym_data.txt"

def load_and_chunk_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on headings like "Title:" or "---"
    chunks = re.split(r"\n-{2,}\n|\nTitle: ", text)
    cleaned_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return cleaned_chunks

def store_embeddings(chunks):
    client = chromadb.PersistentClient(path=".chromadb/")
    try:
        client.delete_collection("gym_chunks")
    except:
        pass
    collection = client.create_collection("gym_chunks")

    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedder.encode(chunks).tolist()
    ids = [f"id_{i}" for i in range(len(chunks))]

    collection.add(documents=chunks, embeddings=embeddings, ids=ids)
    print("[INFO] Embeddings stored successfully.")

if __name__ == "__main__":
    chunks = load_and_chunk_data()
    store_embeddings(chunks)
