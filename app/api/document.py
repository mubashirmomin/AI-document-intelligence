from pathlib import Path
from fastapi import APIRouter,File,HTTPException,UploadFile
from app.services.pdf_service import (
    extract_text_from_pdf,
    save_extracted_text,
    read_extracted_text
)
from app.services.summarization_service import summarize_text
from app.services.translation_service import translate_text
from app.services.qa_services import answer_question
from app.services.notes_service import generate_notes
from app.services.flashcard_service import generate_flashcards


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

@router.get("/summarize/{filename}")
def summarize_document(filename:str):

    text = read_extracted_text(filename)

    summary = summarize_text(text)

    return {
        "filename":filename,
        "summary":summary
    }

@router.get("/translate/{filename}")
def translate_document(filename:str):

    text = read_extracted_text(filename)

    translated_text = translate_text(text)

    return {
        "filename":filename,
        "translated_text":translated_text
    }

@router.get("/ask-question/{filename}")
def ask_question(filename:str,question:str):

    text = read_extracted_text(filename)

    answer = answer_question(
        question=question,
        context=text
    )

    return {
        "filename":filename,
        "question":question,
        "answer":answer
    }

@router.get("/generate-notes/{filename}")
def generate_study_notes(filename:str):

    text = read_extracted_text(filename)

    notes = generate_notes(text)

    return {
        "filename":filename,
        "study_notes":notes
    }

@router.get("/generate-flashcards/{filename}")
def generate_document_flashcards(filename:str):

    text = read_extracted_text(filename)

    flashcards = generate_flashcards(text)

    return {
        "filename":filename,
        "flashcards":flashcards
    }