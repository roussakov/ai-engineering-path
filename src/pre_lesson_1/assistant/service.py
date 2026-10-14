from pydantic_ai import Agent

from pre_lesson_1.assistant.schemas import IntentAnalysis


class AssistentService:

    def __init__(self, agent: Agent[object, IntentAnalysis]) -> None:
        self.agent = agent


    async def analyze_intent(self, message: str) -> IntentAnalysis:
        result = await self.agent.run(message);
        return result.output
