from fastapi import FastAPI, Request
# import json
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from Chat import Chat

app = FastAPI()

# Configuration du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les headers
)

chat_instance = Chat()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send_message/")
async def read_message(request: Request):
  data = await request.json()
  user_message = data.get('message', '')
  print("message reçu : " + user_message)
  bot_response = chat_instance.execute_query(user_message)
  data['response'] = bot_response
  return data