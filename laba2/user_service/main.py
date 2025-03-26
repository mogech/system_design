from fastapi import FastAPI, HTTPException, Depends
from typing import List
from auth import create_token, authenticate_user, users, get_user
from models import User

app = FastAPI()

@app.post("/register")
def register(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.username] = user.password 
    return {"message": "User registered"}

@app.post("/login")
def login(user: User):
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(user.username)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/users", response_model=List[str])
def get_users(current_user: str = Depends(get_user)):
    return list(users.keys())