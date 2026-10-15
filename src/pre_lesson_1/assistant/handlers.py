from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pre_lesson_1.assistant.schemas import (
    AssistantErrorCode,
    AssistantErrorResponse,
    InternalErrorCode,
    InternalErrorResponse,
)
from pre_lesson_1.assistant.service import (
    AssistantExecutionError,
    AssistantUnavailable,
)


def assistant_unavailable_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    body = AssistantErrorResponse(code=AssistantErrorCode.UNAVAILABLE, detail="Assistant is temporarily unavailable")

    return JSONResponse(
        status_code=503,
        content=body.model_dump()
    )

def assistant_execution_error_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    body = InternalErrorResponse(code=InternalErrorCode.INTERNAL_ERROR, detail="Assistant internal error")

    return JSONResponse(
        status_code=503,
        content=body.model_dump()
    )    

def register_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AssistantUnavailable, assistant_unavailable_exception_handler)
    app.add_exception_handler(AssistantExecutionError, assistant_execution_error_exception_handler)