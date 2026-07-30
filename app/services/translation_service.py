from app.services.model import get_translator


def translate_text(text: str):
    translator = get_translator()

    translation = translator(text)

    return translation[0]["translation_text"]