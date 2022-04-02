from fastapi import APIRouter, Query, Depends, Response, status, HTTPException
from typing import Any

from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models.postblog import PostBlog

router = APIRouter()

@router.get("/read")
def read(db:Session = Depends(get_db)):
    blogs = db.query(PostBlog).all()
    return blogs


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_by_id(
    id:int,
    response:Response,
    db: Session = Depends(get_db)
):
    blog = db.query(PostBlog).filter(PostBlog.id==id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"blog with id:{id} is not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {
        #     "msg":response.status_code,
        #     "data": f"blog with id:{id} is not found"
        # }
    return {
        "msg":"ok",
        "data":blog
    }