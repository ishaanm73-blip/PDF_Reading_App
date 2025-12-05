from fastapi import APIRouter, UploadFile, File
from backend.app.ser.embeddings import process_pdf
import os,re
router = APIRouter()
@router.post("/upload")
async def upload_pdf(file:UploadFile=File(...)):
    os.makedirs("temp", exist_ok=True)
    safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", file.filename)
    path = f"temp/{safe_name}"
    file.file.seek(0)
    with open(path, "wb") as f:
        while chunk := file.file.read(1024*1024):
            f.write(chunk)

    chunks = process_pdf(path)

    return {"message": "Uploaded", "chunks": chunks}
