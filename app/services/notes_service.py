from app.services.model import get_text_generator
from app.services.chunking_service import chunk_text


def generate_notes(text:str)->str:
    text_generator = get_text_generator()
    chunks = chunk_text(text)

    notes = []

    for chunk in chunks:
        prompt = f"""
You are an expert professor.

Read the following document and generate concise study notes.

Rules:
- Use bullet points.
- Organize into headings whenever possible.
- Keep only the important information.
- Remove unnecessary details.
- Do not repeat information.

Document:
{chunk}
"""
        result = text_generator(
            prompt,
            max_new_tokens=300,
            do_sample = False
        )

        notes.append(result[0]["generated_text"])
    return "\n\n".join(notes)
