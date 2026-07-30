from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

question_answerer = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2"
)

text_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)