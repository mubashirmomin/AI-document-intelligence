from app.services.model import get_text_generator


def generate_notes(text:str)->str:
    text_generator = get_text_generator()

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
{text}
"""
    result = text_generator(
        prompt,
        max_new_tokens=300,
        do_sample = False
    )

    return result[0]["generated_text"]