from pre_lesson_1.assistant.agent import intent_analyzer_agent
from pre_lesson_1.assistant.service import AssistentService


def get_intent_analyzer_service() -> AssistentService:
    return AssistentService(
        agent=intent_analyzer_agent,
    )