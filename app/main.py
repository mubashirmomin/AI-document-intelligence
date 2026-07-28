from fastapi import FastAPI

app = FastAPI(title="AI Document Intelligence Assitant")

@app.get("/")
def home():
    return {
        "message" : "AI Document Intelligence Assistant is running"
    }