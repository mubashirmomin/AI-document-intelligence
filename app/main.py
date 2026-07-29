from fastapi import FastAPI

from app.api.document import router as document_router

app = FastAPI(title="AI Document Intelligence Assistant")

app.include_router(document_router,prefix="/documents",tags=["Documents"])

@app.get("/")
def home():
    return {
        "message":"AI Document Intelligence Assistant is running "
    }