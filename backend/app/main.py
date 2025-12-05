from fastapi import FastAPI
from backend.app.routers.upload import router as upload_router
from backend.app.routers.ask import router as ask_router
app = FastAPI()
@app.get("/health")
def health():
    return{"status":"ok"}
app.include_router(upload_router, prefix="/api")
app.include_router(ask_router,prefix="/api")