from transformers import pipeline 

question_answerer = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

def answer_question(question:str,context:str) -> str:
    result = question_answerer(
        question=question,
        context=context
    )

    return result["answer"]
