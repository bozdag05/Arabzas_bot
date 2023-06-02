from filters import IsPrivate
from loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.inline import level_markup, lesson_markup, retry_ikb, my_retry_ikb
from utils.db_api import users_commands
from keyboards.default import menu_kb
from keyboards.default import retry_class_word_kb as classes


@dp.message_handler(IsPrivate(), text='Уроки')
async def menu_lesson(message: Message):
    try:
        await message.answer("Выберите уровень:", reply_markup=level_markup)
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(IsPrivate(), text='Свои слова')
async def menu_my_words(message: Message):
    try:
        await message.answer("Выберите уровень:", reply_markup=my_retry_ikb)
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.callback_query_handler(text_contains='level')
async def level_func(call: CallbackQuery):
    try:
        user_id, level = call.from_user.id, int(call.data.split(':')[1])
        await users_commands.update_level(user_id, level)
        await call.message.answer("Выберите урок который хотите повторить:", reply_markup=lesson_markup)
    except Exception:
        await call.message.answer('Что-то не так, попробуйте ещё раз')


@dp.callback_query_handler(text_contains='lesson')
async def lesson_func(call: CallbackQuery):
    try:
        user_id, lesson = call.from_user.id, int(call.data.split(':')[1])
        await users_commands.update_lesson(user_id, lesson)
        await call.message.answer("Выберите вид упражнения:", reply_markup=retry_ikb)
    except Exception:
        await call.message.answer('Что-то не так, попробуйте ещё раз')


@dp.callback_query_handler(text_contains='my_end')
async def my_end_func(call: CallbackQuery):
    try:
        await call.message.answer(f'Повторение завершено!')
        await call.message.edit_reply_markup(my_retry_ikb)
    except Exception:
        await call.message.answer('Что-то не так, попробуйте ещё раз')


@dp.callback_query_handler(text_contains='end')
async def end_func(call: CallbackQuery):
    try:
        await call.message.answer(f'Повторение завершено!')
        await call.message.edit_reply_markup(retry_ikb)
    except Exception:
        await call.message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(IsPrivate(), commands=['end'])
async def end_all(message: Message):
    try:
        await message.answer('Повторение завершено!', reply_markup=classes)
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')
