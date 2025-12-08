from fastapi import APIRouter
from backend.app.ser.embeddings import client

router = APIRouter()

@router.post("/reset")
def reset_collection():
    try:
        client.delete_collection("documents")
    except:
        pass

    client.get_or_create_collection("documents")
    return {"message": "Vector database cleared!"}
