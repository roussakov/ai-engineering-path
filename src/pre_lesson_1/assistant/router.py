from typing import Annotated

from fastapi import APIRouter, Depends, status

from pre_lesson_1.assistant.dependencies import get_intent_analyzer_service
from pre_lesson_1.assistant.schemas import (
    AssistantErrorResponse,
    IntentAnalysis,
    IntentAnalysisRequest,
    InternalErrorResponse,
)
from pre_lesson_1.assistant.service import AssistentService

router = APIRouter(prefix="/assistant")

@router.get("/health")
async def health_check() -> dict[str, str]:
    return {"health" : "ok"}

@router.post("/intent/analyze", responses={
    status.HTTP_503_SERVICE_UNAVAILABLE: {
        "model": AssistantErrorResponse,
        "description": "Assistant service temporarily unavailable"
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "model": InternalErrorResponse,
        "description": "Assistant execution error"
    }
})
async def analyze_intent(
    request: IntentAnalysisRequest, 
    service: Annotated[AssistentService, Depends(get_intent_analyzer_service),]) -> IntentAnalysis:
    return await service.analyze_intent(request.message)
