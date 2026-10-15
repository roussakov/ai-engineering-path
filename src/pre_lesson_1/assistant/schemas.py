from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class InternalErrorCode(StrEnum):
    INTERNAL_ERROR = "INTERNAL_ERROR"

class AssistantErrorCode(StrEnum):
    UNAVAILABLE = "ASSISTANT_UNAVAILABLE"

class InternalErrorResponse(BaseModel):
    code: InternalErrorCode
    detail: str

class AssistantErrorResponse(BaseModel):
    code: AssistantErrorCode
    detail: str

class Intent(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(
        description="A short, descriptive intent name"
    )
    evidence: str = Field(
        description="The exact phrase expressing this intent"
    )

class IntentAnalysis(BaseModel):
    model_config = ConfigDict(extra="forbid")

    primary_intents: list[Intent] = Field(
        description="All primary intents"
    )
    secondary_intents: list[Intent] = Field(
        description=(
            "All additional independent intents found in the message. "
            "Do not omit an intent just because it is less important."
        )
    )
    
    reasoning: str = Field(
        description="A brief explanation supporting the interpretation"
    )

class IntentAnalysisRequest(BaseModel):
    message: str