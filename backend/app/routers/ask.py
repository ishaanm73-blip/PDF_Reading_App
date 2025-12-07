from fastapi import APIRouter, Body
from backend.app.ser.llm import answer
from backend.app.ser.embeddings import search
router = APIRouter()
@router.get("/ask")
def ask(question: str=Body(...),
        history:list[str] = Body(default=[])):
    docs = search(question)
    context = "\n".join(docs)
    conversation_text=""
    for msg in history:
        converation_text += msg + "\n"
    prompt = f"You are a helpful AI assisant who reads the information given, draws conclusions and provides accurate answers based on the context provided.\n\nContext:\n{context}\n\nConversation_History:\n{conversation_text}\n\nQuestion: {question}\n\nAnswer:"
    ans = answer(prompt)
    return {"answer":ans,"context":context}