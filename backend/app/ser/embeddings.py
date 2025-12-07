import chromadb
from backend.app.ser.pdf import extract_text_from_pdf
from sentence_transformers import SentenceTransformer
import os
DB_PATH = "chroma_store"
os.makedirs(DB_PATH, exist_ok=True)
client = chromadb.PersistentClient(path=DB_PATH)
try:
    client.delete_collection("documents")
except Exception as e:
    print("Collection not found or cannot delete:", e)
collection = client.get_or_create_collection(name="documents")

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text,size=800):
        return [text[i:i+size] for i in range(0,len(text),size)]
def process_pdf(path:str):
    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)
    for i, chunk in enumerate(chunks):
        emb = model.encode([chunk]).tolist()[0]
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"{path}_chunk_{i}"])
    return len(chunks)
def search(query:str,top_k=3):
    q_emb = model.encode([query]).tolist()[0]
    results = collection.query(query_embeddings=[q_emb],
                               n_results=top_k)
    return results["documents"][0]