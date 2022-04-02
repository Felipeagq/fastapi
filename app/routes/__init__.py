from fastapi import APIRouter
api_router = APIRouter()

from app.routes.read_route import read_route
api_router.include_router(read_route.router,tags=["Read the Database"])

from app.routes.post_route import post_route
api_router.include_router(post_route.route,tags=["Post a Cedula"])

from app.routes.delete_route import delete_route
api_router.include_router(delete_route.router, tags=["delete a blog"])

from app.routes.update_route import update_route
api_router.include_router(update_route.router, tags=["Update a Post Blog"])