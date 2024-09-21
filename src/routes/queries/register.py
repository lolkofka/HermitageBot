import re
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import config

register_router = Router()

months = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря"
]

weekdays = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
]


@register_router.callback_query(F.data == 'register')
async def register(query: CallbackQuery) -> None:
    await query.answer()
    builder = InlineKeyboardBuilder()

    today = datetime.now()

    for i in range(8):
        day = today + timedelta(days=i)
        builder.button(
            text=f'{day.strftime("%d")} {months[day.month]} {day.strftime("%Y")} ({weekdays[day.weekday()]})',
            callback_data=f'register_{day.strftime("%d.%m.%Y")}')

    builder.adjust(1, repeat=True)
    await query.message.answer('<b>Выберите день, когда вы хотите посетить музей</b>', reply_markup=builder.as_markup())


@register_router.callback_query(F.data.regexp(re.compile(r'^register_(\d{1,2}\.\d{1,2}\.\d{4})$')).as_('match'))
async def register_time(query: CallbackQuery, match: re.Match[str]) -> None:
    day = match.group(1)

    builder = InlineKeyboardBuilder()

    for i in range(12):
        time = f'{i + 9:02}:00'
        builder.button(text=time, callback_data=f'register_{day}_{time}')

    builder.adjust(2, repeat=True)

    await query.message.edit_text('<b>Выберите время визита</b>', reply_markup=builder.as_markup())


@register_router.callback_query(
    F.data.regexp(re.compile(r'^register_(\d{1,2}\.\d{1,2}\.\d{4})_(\d{2}:\d{2})$')).as_('match'))
async def register_complete(query: CallbackQuery, match: re.Match[str]) -> None:
    day, time = match.group(1, 2)

    await query.message.delete()
    await query.answer(f'✅ Вы успешно записаны на {day} {time}!', show_alert=True)

    identity = ''

    if query.from_user.username:
        identity = f'@{query.from_user.username}'

    names = [item for item in [query.from_user.last_name, query.from_user.first_name] if item]

    if len(names) > 0:
        identity += f' ({" ".join(names)})'

    identity += f" [<code>{query.from_user.id}</code>]"

    for admin in config.admins:
        await query.bot.send_message(admin, '🔔 Новая запись!\n'
                                            '\n'
                                            f'👤 Пользователь: {identity}\n'
                                            f'📆 Дата: {day}\n'
                                            f'🕜 Время: {time}\n')
