from transformers import pipeline

notes_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_notes(text:str)->str:

    prompt = f"""
Generate clear and well-structured study notes from the following document.

Document:
{text}
"""
    result = notes_generator(
        prompt,
        max_new_tokens=300,
        do_sample = False
    )

    return result[0]["generated_text"]