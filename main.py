import ProductDatabase
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

ProductDatabase.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    """
    displays the stock screen dashboard/homepage
    """
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/stock")
def create_stock():

    return {
        "code": "success",
        "messsege": "stock created"
    }
