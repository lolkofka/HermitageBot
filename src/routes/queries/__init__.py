from aiogram import Router

from .geolocation import geolocation_router
from .register import register_router

queries_router = Router()

queries_router.include_routers(register_router, geolocation_router)
