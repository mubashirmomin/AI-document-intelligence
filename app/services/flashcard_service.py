from app.services.model import text_generator

def generate_flashcards(text:str)->str:

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
{text}
"""
    result = text_generator(
        text,
        max_new_tokens = 300,
        do_sample=False
    )

    return result[0]["generated_text"]