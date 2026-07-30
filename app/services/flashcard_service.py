from app.services.model import get_text_generator
from app.services.chunking_service import chunk_text

def generate_flashcards(text:str)->str:
    text_generator = get_text_generator()
    chunks = chunk_text(text)
    flashcards = []

    for chunk in chunks:
        prompt = f"""
You are an expert teacher.

Read the document below and create exactly 5 study flashcards.

Rules:
- Each flashcard must have one Question and one Answer.
- Use the information from the document only.
- Rewrite the information in your own words.
- Do NOT copy entire sentences from the document.
- Keep answers short and easy to remember.

Format:

Q: ...
A: ...

Q: ...
A: ...

Document:
{chunk}
"""
        result = text_generator(
            text,
            max_new_tokens = 300,
            do_sample=False
        )

        flashcards.append(result[0]["generated_text"])

    return "\n\n".join(flashcards)