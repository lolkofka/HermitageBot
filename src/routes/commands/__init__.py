from aiogram import Router

from .start import start_router

commands_router = Router()

commands_router.include_router(start_router)
