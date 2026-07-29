from pathlib import Path
from fastapi import APIRouter,File,HTTPException,UploadFile
from app.services.pdf_service import (
    extract_text_from_pdf,
    save_extracted_text
)


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

    try:
        text = extract_text_from_pdf(file_path)

        text_file = save_extracted_text(file.filename,text)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Unable to process PDF: {str(e)}"
        )


    return{
        "message":"file uploaded successfully",
        "filename":file.filename
    }

@router.get("/extract-text/{filename}")
def extract_text(filename:str):
    file_path = UPLOAD_FOLDER/ filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="file not found"
        )

    text = extract_text_from_pdf(file_path)

    return {
        "filename":filename,
        "text":text
    }