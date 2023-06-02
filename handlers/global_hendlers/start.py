from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from filters import IsPrivate
from states.state_test_1 import state_1, callback
from utils.db_api import users_commands as commands, users_commands
from keyboards.default import retry_class_word_kb as classes, menu_kb

from loader import dp, bot


@dp.message_handler(IsPrivate(), commands=['start'])
async def start(message: Message):
    await message.answer('السلام عليكم و رحمة الله و بركاته')
    await message.answer(f'Добро пожаловать, на телеграм бот по изучению и повторению арабских слов\n\n'
                         f'Нажмите на одну из команд:\n\n'
                         f'Упражнения - /type_tests\n\n'
                         f'Информация о боте - /info\n'
                         f'Помощь - /help\n')
    try:
        user = await commands.select_user(message.from_user.id)
        if user == None:
            await commands.add_user(
                user_id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                level=0,
                lesson=0,
                status='user',
                )
            await bot.send_message(chat_id=1096151413, text=f'Зарегистрировался пользователь - {message.from_user.username}\n\n'
                                                            f'ID: {message.from_user.id}'
                                                            f'Имя: {message.from_user.first_name}\n\n'
                                                            f'Фамилия: {message.from_user.last_name}\n\n')
    except Exception:
        return


@dp.message_handler(IsPrivate(), commands=['help'])
async def help(message: Message):
    await message.answer(
        f'/info -- Информация о боте\n\n'
        f'/menu_user -- Меню пользователя для работы со своим словарём (добавления удаление слов в словарь и т.д.)\n\n'
        f'/type_tests -- Виды упражнений\n\n'
        f'/callback -- Обратная связь с админом\n\n'
        f'/end -- Завершить упражнение во время выполнения\n'
    )


@dp.message_handler(IsPrivate(), commands=['type_tests'])
async def type_tests(message: Message):
    try:
        await message.answer('Выберите что хотите повторить:', reply_markup=classes)
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(IsPrivate(), commands=['menu_user'])
async def menu_replay(message: Message):
    try:
        await message.answer("Выберите действие:", reply_markup=menu_kb)
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(IsPrivate(), commands=['info'])
async def info(message: Message):
    await message.answer(
        'Бот является вспомогательным инструментом для упражнения над словами, пройденными на курсе «Арабский для начинающих».\n\n'
        'Также бот даёт возможность создать свой собственный словарь.\n\n'
        )


@dp.message_handler(IsPrivate(), commands=['callback'])
async def callback_from_admin(message: Message):

    try:
        user_id = message.from_user.id
        user = await users_commands.select_user(user_id)
        if user.status != 'ban':
            await message.answer('Напишите сообщение которое хотите отправить админу')
            await callback.callback_from_admin.set()
        else:
            await message.answer('Вы не можете отправит сообщение')

    except Exception:
            await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(state=callback.callback_from_admin)
async def call_admin(message: Message, state: FSMContext):

    try:
        answer, user_id = message.text, message.from_user.id
        user = await users_commands.select_user(user_id)
        await bot.send_message(
            chat_id=1096151413,
            text=f'ID: {user_id}\n\n'
                 f'Имя: {user.first_name}\n'
                 f'Фамилия: {user.last_name}\n'
                 f'Статус: {user.status}\n'
        )
        await bot.send_message(chat_id=1096151413, text=answer)
        await message.answer('Сообщение отправлено')

    except Exception:
        await state.finish()
        await message.answer("Сообщение не получилось отправить ")

    await state.finish()

