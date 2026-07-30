from app.services.model import get_question_answerer

def answer_question(question:str,context:str) -> str:
    result = question_answerer(
        question=question,
        context=context
    )

    return result["answer"]
