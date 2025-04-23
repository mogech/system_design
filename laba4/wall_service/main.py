from fastapi import FastAPI, Depends, HTTPException
from auth import get_user
from typing import List
from models import WallPost
import crud

app = FastAPI()

@app.post("/posts", response_model=WallPost)
def create_post(post: WallPost, current_user: str = Depends(get_user)):
    post.author = current_user
    return crud.create_post(post)

@app.get("/posts", response_model=List[WallPost])
def get_all(current_user: str = Depends(get_user)):
    return crud.get_posts()

@app.get("/posts/{post_id}", response_model=WallPost)
def get_by_id(post_id: str, current_user: str = Depends(get_user)):
    post = crud.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.delete("/posts/{post_id}")
def delete(post_id: str, current_user: str = Depends(get_user)):
    success = crud.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Deleted"}