from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.chatbot import get_chat_response
from app.models import ChatRequest

router = APIRouter()

templates = Jinja2Templates(directory="templates")


# Home Page
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Health Check
@router.get("/health")
def health():
    return {
        "status": "ok",
        "message": "SHL AI Chatbot is running"
    }


# Chat API
@router.post("/chat")
def chat(request: ChatRequest):
    return get_chat_response(request.message)