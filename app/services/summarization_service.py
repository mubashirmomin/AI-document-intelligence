from app.services.model import get_summarizer
from app.services.chunking_service import chunk_text

def summarize_text(text:str):
    summarizer = get_summarizer()

    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        summary = summarizer(
            text,
            max_length = 150,
            min_length = 40,
            do_sample = False
        )
        summaries.append(summary[0]["summary_text"])

    final_summary = "\n\n".join(summaries)
    
    return final_summary