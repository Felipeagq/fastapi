

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import settings


# Creamos el motor 
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={
        "check_same_thread":False
    }
)

# la sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#
# Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()