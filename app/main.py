from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.rag import retrieve_relevant_chunks, generate_answer

app = FastAPI(title="Gym RAG Chatbot")

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str
    source_chunks: Optional[List[str]] = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        chunks = retrieve_relevant_chunks(request.query)
        if not chunks:
            return ChatResponse(response="Sorry, I couldn't find anything relevant.")

        answer = generate_answer(request.query, chunks)
        return ChatResponse(response=answer, source_chunks=chunks)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/reset")
def reset():
    # Placeholder – no session state used
    return {"status": "conversation reset"}
