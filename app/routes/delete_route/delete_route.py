from fastapi import APIRouter, status, Depends,Path,Query,Body
from typing import Optional,List

from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models.postblog import PostBlog

from pydantic import BaseModel

router = APIRouter()

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_route(
    id:int,
    db: Session = Depends(get_db)
):
    blog = db.query(PostBlog).filter(PostBlog.id == id).delete(synchronize_session=False)
    db.commit()
    return {
        "msg":"ok",
        "data":{
            "delete":id
        }
    }
