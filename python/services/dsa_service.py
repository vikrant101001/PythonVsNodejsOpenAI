from models.dsa_request import QuestionRequest
from services.openai_service import OpenAIService

class DsaService:
    def __init__(self, openai_service: OpenAIService):
        self.openai_service = openai_service

    def analyze_question(self, question_request: QuestionRequest):
        base_prompt = """
        You are a DSA expert. Given a question related to Data Structures and Algorithms (DSA),
        identify the topics being asked and provide an explanation for it. Respond in a structured
        format with a list of topics and an explanation.
        """
        full_prompt = f"{base_prompt}\n\nQuestion: {question_request.question}"
        analysis = self.openai_service.analyze_dsa(full_prompt)
        return analysis
