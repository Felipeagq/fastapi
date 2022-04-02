from datetime import datetime

from fastapi import APIRouter, Body, Depends, status
from app.schemas.posteo import Posteo

from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models.postblog import PostBlog

route = APIRouter()



@route.post("/post/", status_code = status.HTTP_201_CREATED)
def post_route(
    posteo:Posteo = Body(...,
        description="JSON para crear un Posteo en el Blog",
        title="creación posteo",
        embed=True
        ),
    db: Session = Depends(get_db)
    ):

    new_blog = PostBlog(
        name= posteo.name,
        body= posteo.body,
        date = posteo.date
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {
        "msg":"ok",
        "post":new_blog
        }