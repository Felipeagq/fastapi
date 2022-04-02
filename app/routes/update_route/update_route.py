from fastapi import APIRouter, Depends
from app.schemas.posteo import Posteo

from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models.postblog import PostBlog

router = APIRouter()

@router.put("/update/{id}")
def update_route(
    id:int,
    body : Posteo,
    db: Session = Depends(get_db)
):
    return {
        "id":id,
        "body":body
    }