from fastapi import APIRouter, HTTPException
from models.dsa_request import QuestionRequest
from services.dsa_service import DsaService
from services.openai_service import OpenAIService

class DsaController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/analyze_dsa", self.analyze_dsa, methods=["POST"])
        openai_service = OpenAIService(api_key="your_openai_api_key_here", model="gpt-3.5-turbo")
        self.dsa_service = DsaService(openai_service=openai_service)

    async def analyze_dsa(self, question_request: QuestionRequest):
        try:
            analysis = self.dsa_service.analyze_question(question_request)
            return {"question": question_request.question, "analysis": analysis}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
