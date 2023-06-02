from aiogram.types import Message
from data.config import admins_id
from loader import dp, bot
from utils.db_api.db_global import on_startup
from loader import db


@dp.message_handler(commands=['Connection_from_postgreSQL'])
async def connection(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            print("Подключение к БД")
            await on_startup(dp)
            await message.answer('Подключение к БД')

    except Exception:
        await message.answer('Error')


@dp.message_handler(commands=['Delete_from_postgreSQL'])
async def delete(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            print("Удаляем таблицы в БД")
            await db.gino.drop_all()
            await message.answer('Удаляем таблицы в БД')
    except Exception:
        await message.answer('Error')


@dp.message_handler(commands=['Create_from_postgreSQL'])
async def create(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            print("Создаём новые таблицы в БД")
            await db.gino.create_all()
            await message.answer('Создаём новые таблицы в БД')
    except Exception:
        await message.answer('Error')