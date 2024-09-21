from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from assets import cover

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message) -> None:
    builder = InlineKeyboardBuilder()

    builder.button(text='🎟️ Купить билет', url='https://tickets.hermitagemuseum.org')
    builder.button(text='📍 Геолокация', callback_data='geolocation')
    builder.button(text='📆 Записаться', callback_data='register')

    builder.adjust(1, repeat=True)

    await message.answer_photo(cover,
                               'Здравствуйте! Вас приветствует бот для записи в Эрмитаж - российский государственный художественный'
                               ' и культурно-исторический музей в Санкт-Петербурге, '
                               'одно из крупнейших в мире учреждений подобного рода.\n'
                               '\n'
                               '<b>Часы работы:</b>\n'
                               'Пн-Вс 9:00-21:00\n'
                               '\n'
                               'Для записи, нажмите на кнопку ниже', reply_markup=builder.as_markup())
