from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

def translate_text(text:str):
    translation = translator(
    text,
    truncation=True,
    max_length=512
)

    return translation[0]["translation_text"]