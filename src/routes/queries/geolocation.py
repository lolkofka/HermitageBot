from aiogram import Router, F
from aiogram.types import CallbackQuery

geolocation_router = Router()


@geolocation_router.callback_query(F.data == 'geolocation')
async def geolocation(query: CallbackQuery) -> None:
    await query.answer()
    await query.message.answer('Дворцовая площадь, 2, Санкт-Петербург\n'
                               '\n'
                               '🚇 Адмиралтейская')
    await query.message.answer_location(59.939939, 30.314488)
