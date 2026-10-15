from fastapi import FastAPI

from pre_lesson_1 import assistant

app = FastAPI()

app.include_router(assistant.router)

assistant.register_handlers(app);