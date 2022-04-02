from pydantic import BaseModel
from datetime import datetime

class Posteo(BaseModel):
    id:int
    name:str
    apellido:str
    cedula:int
    date:datetime
    