import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import ApiWrapper

app = FastAPI()
api = ApiWrapper("https://backend.cube-hackaton.ru")
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    params = {'request': request, 'title': 'Главная'}
    return templates.TemplateResponse("index.html", params)


@app.get("/tours", response_class=HTMLResponse)
async def tours(request: Request):
    params = {'request': request, 'title': 'Туры'}
    requests.get("http://127.0.0.1:8000/api/getLooks/").json()
    return templates.TemplateResponse("tours.html", params)