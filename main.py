from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Optional

app = FastAPI()

# Подключаем путь до шаблона
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


# Функция обработки URL по get запросу
@app.get("/", response_class=HTMLResponse)
async def hello(request: Request, name: Optional[str] = None, message: Optional[str] = None):
    error = {"Error": "Name or message field is required"}
    if name and message:
        return templates.TemplateResponse("iter.html", {"request": request, "name": name, "message": message})
    return error
