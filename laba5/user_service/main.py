from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from auth import create_token, authenticate_user, get_user
from database import SessionLocal, engine
import crud

from models import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    crud.create_user(db, user.username, user.password)
    return {"message": "User registered"}

@app.post("/login")
def login(user: User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user or not authenticate_user(user.username, user.password, db):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(user.username)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/users")
def get_users(current_user: str = Depends(get_user), db: Session = Depends(get_db)):
    return [user.username for user in crud.get_all_users(db)]

@app.get("/user/{username}")
def get_user_by_name(username: str, current_user: str = Depends(get_user), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username}
