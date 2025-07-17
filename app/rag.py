# app/rag.py
import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
import requests

load_dotenv()

embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=".chromadb/") 
collection = client.get_or_create_collection("gym_chunks")

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")

def retrieve_relevant_chunks(query, top_k=3):
    query_embedding = embedder.encode([query])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    chunks = results['documents'][0]
    
    print("\n[Retrieved Chunks for Debugging]:")
    for i, chunk in enumerate(chunks):
        print(f"{i+1}. {chunk[:100]}...")  # print first 100 characters

    return chunks

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""
You are a helpful fitness assistant. Answer the user's question based on the context below. Only use the context to answer. If the question is unrelated to gym, fitness, equipment, or exercises, respond with: "Sorry, I can only answer gym-related questions."

Context:
{context}

Question:
{query}

Answer:
"""

    url = "https://api.fireworks.ai/inference/v1/completions"
    headers = {
        "Authorization": f"Bearer {FIREWORKS_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "accounts/fireworks/models/llama4-maverick-instruct-basic",  # Free open LLM
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0.7
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()["choices"][0]["text"].strip()


if __name__ == "__main__":
    query = input("Ask a gym-related question: ")
    chunks = retrieve_relevant_chunks(query)
    print("\n[Retrieved Context]:")
    for chunk in chunks:
        print("-", chunk)

    answer = generate_answer(query, chunks)
    print("\n[Generated Answer]:")
    print(answer)
