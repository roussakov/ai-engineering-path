# AI Engineering Path

A collection of hands-on AI engineering assignments built with Python. The current project explores integrating a locally hosted large language model (LLM) into a FastAPI application using Pydantic AI, with structured JSON responses for intent analysis.

## Scenario: intent analysis

The current assignment implements an **intent-analysis REST API**. A client submits a natural-language message, and a locally running LLM identifies the user's expressed intentions and returns structured JSON instead of an unstructured chat response.

The analysis aims to:

- Recognize explicit and sufficiently supported implicit intents in the **entire** message.
- Distinguish primary intents from secondary ones, including cases with equally important primary intents.
- Include a verbatim supporting phrase (`evidence`) for each detected intent.
- Avoid inventing intentions or treating prompt-injection instructions as authoritative.

For example, the message *“I want to study but I will grab a coffee first”* can express a longer-term goal (studying) and an immediate action (getting coffee). Deciding how to prioritize these is part of the assignment; the model's output can vary, and classification quality is evaluated through test prompts.

## Tech stack

- **Python 3.14** — application language
- **FastAPI** — REST API and interactive OpenAPI documentation
- **Pydantic AI** — LLM integration and structured outputs
- **Docker Compose** — local LLM inference server
- **uv** — Python dependency and environment management
- **Ruff & Pyright** — linting and static type checking

## Prerequisites

- Python 3.14
- [uv](https://docs.astral.sh/uv/)
- Docker with Docker Compose support

## Getting started

Run the following commands from the repository root unless noted otherwise.

### 1. Clone the repository

```bash
git clone https://github.com/roussakov/ai-engineering-path.git
cd ai-engineering-path
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the repository root:

```dotenv
LLM_URL=http://localhost:8080/v1
LLM_MODEL=ai/qwen3
```

`LLM_URL` is the OpenAI-compatible API endpoint exposed by the local inference server. `LLM_MODEL` specifies which model the application requests.

### 4. Start the LLM inference server

**Start Docker Compose before running FastAPI.** The API depends on the local LLM service being available.

```bash
docker compose up -d
```

To watch the service logs:

```bash
docker compose logs -f
```

> Run these commands from the directory containing the project's Compose configuration. The LLM service must expose its API at `http://localhost:8080/v1` to match `.env`.

### 5. Start the FastAPI application

In another terminal, from the repository root:

```bash
uv run fastapi dev
```

The development server runs at **http://127.0.0.1:8000** by default.

- API docs (Swagger UI): http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json

## Run and explore API requests

Once FastAPI is running, you can execute API requests directly from the interactive Swagger UI:

**[Analyze Intent — Swagger UI](http://localhost:8000/docs#/default/analyze_intent_assistant_intent_analyze_post)**

Open the endpoint, select **Try it out**, enter a request payload, and click **Execute** to inspect the response.

### Example request and response

With the LLM server and FastAPI running, send a request to the intent-analysis endpoint:

```bash
curl -X POST "http://localhost:8000/assistant/intent/analyze" \
  -H "Content-Type: application/json" \
  -d '{"message":"I want to study, but I also need to rest."}'
```

An **illustrative** successful JSON response (wording and ordering may differ between LLM runs):

```json
{
  "primary_intents": [
    {
      "name": "study",
      "evidence": "I want to study"
    }
  ],
  "secondary_intents": [
    {
      "name": "rest",
      "evidence": "I also need to rest"
    }
  ],
  "reasoning": "The speaker expresses a goal to study and a separate need to rest."
}
```

The classification and generated labels are model-dependent; the example demonstrates the expected *shape* of the result, not a guaranteed exact response. You can also run this request in [Swagger UI](http://localhost:8000/docs#/default/analyze_intent_assistant_intent_analyze_post), which displays the current endpoint schema and example payload fields.

## Prompt examples

Example prompts for experimenting with the intent analysis API are available in the repository's **[prompts directory](https://github.com/roussakov/ai-engineering-path/blob/master/prompts)**.

## Development checks

```bash
uv run ruff check .
uv run pyright
```

## Stopping the services

Stop FastAPI with `Ctrl+C`, then stop the Docker services:

```bash
docker compose down
```

## Project status

This is a learning repository. Assignments and implementation details will evolve as new AI engineering concepts are explored.
