import chromadb
from backend.app.ser.pdf import extract_text_from_pdf
from sentence_transformers import SentenceTransformer
DB_PATH = "chroma_store"
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name="documents")

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text,size=800):
    for i in range(0,len(text),size):
        return [text[i:i+size]]