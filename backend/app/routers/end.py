from fastapi import APIRouter
from backend.app.ser.embeddings import client
router = APIRouter()
@router.get("/clear")
def clear_data():
    client.reset()
    return{"message":"DataCleared"}