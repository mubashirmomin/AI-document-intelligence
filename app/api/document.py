from pathlib import Path
from fastapi import APIRouter,File,HTTPException,UploadFile

router = APIRouter()

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only Pdf Files are allowed"
        )
    file_path = UPLOAD_FOLDER/file.filename

    with open(file_path,"wb") as pdf_file:
        content = await file.read()
        pdf_file.write(content)

    return{
        "message":"file uploaded successfully",
        "filename":file.filename
    }