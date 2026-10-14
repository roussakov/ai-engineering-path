from typing import Annotated

from fastapi import APIRouter, Depends

from pre_lesson_1.assistant.dependencies import get_intent_analyzer_service
from pre_lesson_1.assistant.schemas import IntentAnalysis, IntentAnalysisRequest
from pre_lesson_1.assistant.service import AssistentService

router = APIRouter(prefix="/assistant")

@router.get("/health")
async def health_check() -> dict[str, str]:
    return {"health" : "ok"}

@router.post("/intent/analyze")
async def analyze_intent(
    request: IntentAnalysisRequest, 
    service: Annotated[AssistentService, Depends(get_intent_analyzer_service),]) -> IntentAnalysis:
    return await service.analyze_intent(request.message)