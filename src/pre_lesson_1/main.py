from fastapi import FastAPI

from pre_lesson_1.assistant.router import router

app = FastAPI()

app.include_router(router)