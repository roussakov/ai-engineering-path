from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from pre_lesson_1.assistant.schemas import IntentAnalysis
from pre_lesson_1.settings import settings

model = OpenAIChatModel(
    model_name=settings.llm_model,
    provider=OpenAIProvider(
        base_url=settings.llm_url,
        api_key="local",
    ),
)

intent_analyzer_agent = Agent(
    model=model,
    output_type=IntentAnalysis,
    instructions="""
    You are an intent analysis agent.

    Identify ALL distinct intents expressed by the user.

    Rules:
    1. Analyze the entire message before selecting the primary intent.
    2. Detect independent requests, needs, and emotional expressions.
    3. Choose the most urgent or central intent as primary.
    4. Put every other distinct intent into secondary_intents.
    5. Do not ignore casual, indirect, or low-priority intents.
    6. Secondary intents can be empty when only one intent exists.
    7. Include the exact supporting phrase for each intent.
    """,
)