from app.services.model import get_text_generator

def generate_quiz(text:str)->str:
    text_generator = get_text_generator()

    prompt = f"""
You are an expert teacher.

Read the document below and generate exactly 5 multiple-choice questions.

Rules:
- Each question must have four options (A, B, C, D).
- Clearly mention the correct answer.
- Use only the information from the document.
- Do not invent facts.

Format:

Question:
...

A.
B.
C.
D.

Answer:

Document:
{text}
"""
    result = text_generator(
        prompt,
        max_new_tokens = 400,
        do_sample = False
    )

    return result[0]["generated_text"]