from fastapi import FastAPI, HTTPException, status
from typing import Literal

from app import __version__
from app.schemas import PostResponse
from sample_data import posts


app = FastAPI()


@app.get("/api/version")
def version() -> dict[Literal["version"], str]:
    return {"version": __version__}


@app.get("/api/posts", response_model=list[PostResponse])
def get_posts():
    return posts


@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
