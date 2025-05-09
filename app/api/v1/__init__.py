from urllib.response import addbase

from fastapi import APIRouter
from app.api.v1.endpoints import user,address

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(address.router)