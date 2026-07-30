from transformers import pipeline

summarizer = None
translator = None
question_answerer = None
text_generator = None

def get_summarizer():
    global summarizer

    if summarizer is None:
        print("Loading Summarizer")
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    return summarizer

def get_translator():
    global translator

    if translator is None:
        print("Loading Translator...")
        translator = pipeline(
            "translation",
            model="Helsinki-NLP/opus-mt-en-fr"
        )

    return translator


def get_question_answerer():
    global question_answerer

    if question_answerer is None:
        print("Loading Question Answering Model...")
        question_answerer = pipeline(
            "question-answering",
            model="deepset/roberta-base-squad2"
        )

    return question_answerer


def get_text_generator():
    global text_generator

    if text_generator is None:
        print("Loading Text Generator...")
        text_generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

    return text_generator