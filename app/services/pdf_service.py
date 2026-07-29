from pathlib import Path

import fitz

def extract_text_from_pdf(pdf_path:Path) -> str:
    document = fitz.open(pdf_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    return extracted_text.strip()

def save_extracted_text(pdf_filename:str,text:str) -> Path:
    output_folder = Path("extracted_text")
    output_folder.mkdir(exist_ok=True)

    text_file = output_folder / f"{Path(pdf_filename).stem}.txt"

    with open(text_file,"w",encoding="utf-8") as file:
        file.write(text)

    return text_file