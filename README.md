# FastAPI

### Migraciones
- pip install alembic
- alembic init migration
- comentar "# sqlalchemy.url = ..."
- en migration/env.py importo la clase Base de app.database.databse
target_metadata = Base.metadata
-  comento "# Base.metadata.create_all(engine)" en el entrypoint.py
- configurar en env.py
- alembic current -> carpeta version
- alembic revision --autogenerate -m "first m"
- alembic upgrade head 