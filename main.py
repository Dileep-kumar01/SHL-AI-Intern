from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import router

app = FastAPI(
    title="SHL AI Chatbot",
    version="1.0.0"
)

# Serve CSS files
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)