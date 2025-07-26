from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import database, crud, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Chatbot backend is running!"}
