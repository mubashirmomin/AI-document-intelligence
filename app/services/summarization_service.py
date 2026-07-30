from app.services.model import get_summarizer

def summarize_text(text:str):
    summarizer = get_summarizer()
    summary = summarizer(
        text,
        max_length = 150,
        min_length = 40,
        do_sample = False
    )

    return summary[0]["summary_text"]