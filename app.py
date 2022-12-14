from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import json
from datetime import datetime, timedelta
#from models import Crypto
#from database import engine
from sqlalchemy.orm import sessionmaker

#Session = sessionmaker(bind=engine)
#session = Session()

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# uvicorn app:app --reload

@app.get("/")
def index(request: Request):
    balance = 1
    return templates.TemplateResponse("chotaresp.html", {"request": request, "balance" : balance})

@app.get("/forum")
def forum(request: Request):
    
    return templates.TemplateResponse("forum.html", {"request": request})