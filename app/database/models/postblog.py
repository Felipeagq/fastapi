from sqlalchemy import Column, Integer, String
from app.database.base_class import Base

class PostBlog(Base):
    __tablename__= "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    body = Column(String)
    date = Column(String)