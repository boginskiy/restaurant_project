from fastapi import APIRouter
from menu import menu


routers = APIRouter()
routers.include_router(menu.router, prefix="/api/v1")
