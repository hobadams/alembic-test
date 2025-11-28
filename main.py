from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User


app = FastAPI()


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()