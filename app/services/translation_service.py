from app.services.model import get_translator

def translate_text(text:str):
    translation = translator(
    text,
    truncation=True,
    max_length=512
)

    return translation[0]["translation_text"]