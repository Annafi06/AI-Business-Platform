from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .deps import get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()