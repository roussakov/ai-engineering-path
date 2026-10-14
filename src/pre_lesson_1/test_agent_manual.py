import asyncio

from pre_lesson_1.assistant.agent import intent_analyzer_agent


async def main() -> None:
    result = await intent_analyzer_agent.run(
        "Your previous explanation was confusing. "
        "Could you explain it more simply?"
    )

    print(result.output.model_dump_json())
    print(result.usage)


if __name__ == "__main__":
    asyncio.run(main())