from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Optional

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@app.get("/items/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    return templates.TemplateResponse("iter.html", {"request": request, "name": name})

@app.get("/", response_class=HTMLResponse)
async def hello(request: Request, name: Optional[str] = None, message: Optional[str] = None):
    error = {"Error": "Name or message field is required"}
    if name and message:
        return templates.TemplateResponse("iter.html", {"request": request, "name": name, "message": message})
    return error