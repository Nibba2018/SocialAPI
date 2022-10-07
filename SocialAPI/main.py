from typing import Optional

from fastapi import FastAPI, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session

from SocialAPI import models
from SocialAPI.db import engine, get_db
from SocialAPI.schemas import Post

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get('/')
async def root():
    return {'message': "Hello World"}


@app.get('/posts')
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@app.get('/posts/{id}')
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"data": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id_: int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('posts/{id}')
def update_post(id: int):
    return {"data", id}

