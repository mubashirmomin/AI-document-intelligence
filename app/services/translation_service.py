from app.services.model import get_translator
from app.services.chunking_service import chunk_text


def translate_text(text: str):
    translator = get_translator()

    chunks = chunk_text(text)
    translate_chunks = []

    for chunk in chunks:
        translation = translator(chunk)

        translate_chunks.append(translation[0]["translation_text"])


    return "\n\n".join(translate_chunks)