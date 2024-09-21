from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import config
from routes import commands_router, queries_router

bot = Bot(config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.include_routers(commands_router, queries_router)


async def start():
    await dp.start_polling(bot)
