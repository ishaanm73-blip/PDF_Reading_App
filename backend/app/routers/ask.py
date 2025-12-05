from fastapi import APIRouter
from backend.app.ser.llm import answer
from backend.app.ser.embeddings import search
router = APIRouter()
@router.get("/ask")
def ask(question: str):
    docs = search(question)
    context = "\n".join(docs)
    ans = answer(question,context)
    return {"answer":ans,"context":context}