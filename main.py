import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    params = {'request': request, 'title': 'Главная'}
    return templates.TemplateResponse("index.html", params)


@app.get("/tours", response_class=HTMLResponse)
async def tours(request: Request):
    user_tours = []
    of_tours = []
    tours = []
    for i in tours:
        if i.flag == True:
            user_tours.append(i)
            continue
        of_tours.append(i)
    user_tours = [user_tours[i:i + 3] for i in range(0, len(user_tours), 3)]
    of_tours = [of_tours[i:i + 3] for i in range(0, len(of_tours), 3)]
    tours = [tours[i:i + 3] for i in range(0, len(tours), 3)]
    params = {'request': request, 'title': 'Туры', 'user_tours': user_tours, 'of_tours': of_tours, 'tours': tours}
    requests.get("http://127.0.0.1:8000/api/getLooks/").json()
    return templates.TemplateResponse("tours.html", params)