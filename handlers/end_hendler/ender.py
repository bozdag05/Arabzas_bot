from loader import dp
from aiogram.types import Message


@dp.message_handler()
async def all_message(message: Message):
        await message.answer('Не вводите что попало, обратитесь к меню по команде  /start')

