from pydantic_ai import Agent
from pydantic_ai.exceptions import UsageLimitExceeded

from pre_lesson_1.assistant.schemas import IntentAnalysis


class AssistantUnavailable(Exception):
    pass

class AssistantExecutionError(Exception):
    pass

class AssistentService:

    def __init__(self, agent: Agent[object, IntentAnalysis]) -> None:
        self.agent = agent


    async def analyze_intent(self, message: str) -> IntentAnalysis:
        try:
            result = await self.agent.run(message);
            # Trigger UsageLimitExceeded scenario
            # result = await self.agent.run(message, usage_limits=UsageLimits(total_tokens_limit=1));
            return result.output
        except UsageLimitExceeded as exc:
            print(exc) # mock-logging
            raise AssistantExecutionError("Agent exceeded its execution budget") from exc
        except Exception as exc:
            print(exc); # mock-logging
            raise AssistantUnavailable() from exc
