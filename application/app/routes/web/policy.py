from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request


templates = Jinja2Templates(directory="app/templates")

policy_web_route = APIRouter()


@policy_web_route.get("/", response_class=HTMLResponse)
async def show_policy(request: Request):
    return templates.TemplateResponse("policy2.html", {"request": request})
