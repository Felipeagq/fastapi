from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.settings import settings
from app.routes import api_router

from app.database.models import postblog
from app.database.database import engine

# Creación de la aplicación
app = FastAPI(
    title = settings.PROJECT_NAME,
    version = settings.PROJECT_VERSION
)

# Configuración de los CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins= [str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"]
    )

# Inclusión de rutas
app.include_router(api_router, prefix=settings.API_V1_STR)

# Creamos la tabla
# Base.metadata.create_all(engine)