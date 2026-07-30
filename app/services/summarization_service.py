from app.services.model import summarizer

def summarize_text(text:str):
    summary = summarizer(
        text,
        max_length = 150,
        min_length = 40,
        do_sample = False
    )

    return summary[0]["summary_text"]