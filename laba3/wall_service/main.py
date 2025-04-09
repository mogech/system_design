from fastapi import FastAPI, Depends, HTTPException
from typing import List
from models import WallPost
from auth import get_user 

app = FastAPI()

wall_posts = []

@app.post("/posts", response_model=WallPost)
def create_post(post: WallPost, current_user: str = Depends(get_user)):
    post.author = current_user
    post.id = len(wall_posts) + 1
    wall_posts.append(post)
    return post

@app.get("/posts", response_model=List[WallPost])
def get_posts(current_user: str = Depends(get_user)):
    return wall_posts