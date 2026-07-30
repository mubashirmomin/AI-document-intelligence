from textwrap import wrap

def chunk_text(text:str , chunk_size: int=400):
    chunks = wrap(
        text,
        width=chunk_size,
        break_long_words=False,
        replace_whitespace=False
    )

    return chunks