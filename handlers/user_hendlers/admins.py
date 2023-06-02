from aiogram.dispatcher import FSMContext
from data.config import admins_id
from filters import IsPrivate
from states.state_test_1 import callback
from states.state_test_1 import admin_state, word_state
from utils.db_api import word_commands as commands, users_commands
from loader import dp, bot
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(IsPrivate(), commands=['add_words'])
async def add_level(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            await message.answer('enter level')
            await word_state.level_state.set()
        else:
            user = await users_commands.select_user(user_id)
            if user.status == 'admin':
                await message.answer('enter level')
                await word_state.level_state.set()

    except Exception:
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), state=word_state.level_state)
async def down(message: Message, state: FSMContext):
    try:
        answer = message.text
        await state.update_data(level_state=answer)
        await message.answer('enter lesson')
        await word_state.lesson_state.set()

    except Exception:
        await state.finish()
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), state=word_state.lesson_state)
async def down(message: Message, state: FSMContext):
    try:
        answer = message.text
        await state.update_data(lesson_state=answer)
        await message.answer('enter words by ,')
        await word_state.word_state.set()

    except Exception:
        await state.finish()
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), state=word_state.word_state)
async def down(message: Message, state: FSMContext):
    try:
        answer = message.text
        await state.update_data(word_state=answer)
        await message.answer('enter translations by ,')
        await word_state.translation_state.set()

    except Exception:
        await state.finish()
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), state=word_state.translation_state)
async def down(message: Message, state: FSMContext):
    try:
        answer = message.text
        await state.update_data(translation_state=answer)

        data = await state.get_data()
        level, lesson, words, translations = int(data.get('level_state')), int(data.get('lesson_state')), data.get(
            'word_state'), data.get('translation_state')

        words, translations = words.split(', '), translations.split(', ')

        for k, word in enumerate(words):
            word_id = await commands.select_all()
            await commands.add_word(
                word_id=int(word_id) + 1,
                level=level,
                lesson=lesson,
                word=word.lower(),
                translation=translations[k].lower(),

            )

        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1,
                                     keyboard=[
                                         [
                                             KeyboardButton('/add_words')
                                         ]
                                     ])
        await message.answer('again', reply_markup=markup)

    except Exception:
        await state.finish()
        await message.answer('Error admins')

    await state.finish()


@dp.message_handler(IsPrivate(), commands=['delete'])
async def get_id(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            await message.answer('enter ID')
            await admin_state.get_id_state.set()
        else:
            user = await users_commands.select_user(user_id)
            if user.status == 'admin':
                await message.answer('enter ID')
                await admin_state.get_id_state.set()

    except Exception:
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), state=admin_state.get_id_state)
async def delete_word(message: Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            answer = int(message.text)

            await commands.delete_word(answer)
            await message.answer('OK')
            await state.finish()

    except Exception:
        await state.finish()
        await message.answer('Error')

    await state.finish()


@dp.message_handler(IsPrivate(), commands=['all'])
async def get_id(message: Message):
    try:

        user_id = message.from_user.id
        if user_id in admins_id:
            await message.answer('enter level, lesson')
            await admin_state.get_level_lesson.set()

        else:
            user = await users_commands.select_user(user_id)
            if user.status == 'admin':
                await message.answer('enter level, lesson')
                await admin_state.get_level_lesson.set()

    except Exception:
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), state=admin_state.get_level_lesson)
async def delete_word(message: Message, state: FSMContext):
    try:
        level, lesson = int(message.text.split()[0]), int(message.text.split()[1])
        words = await commands.select_lesson_words(level, lesson)
        for word in words:
            await message.answer(
                f'ID: {word.word_id}\n\n'
                f'level: {word.level}; lesson: {word.lesson}\n'
                f'word: {word.word}\n'
                f'translation: {word.translation}'
            )
        await message.answer('OK')
        await state.finish()

    except Exception:
        await state.finish()
        await message.answer('Error admins')

    await state.finish()


@dp.message_handler(IsPrivate(), commands=['get_admins_commands'])
async def get_commands(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            await message.answer('/add_words - Добавить слова\n\n'
                                 '/all - Получить все слова\n\n'
                                 '/delete - Удалить все слова\n\n'
                                 '/callback_with_user - Связь с пользователем\n\n'
                                 '/update_status - Поменять статус\n\n',
                                 )
        else:
            user = await users_commands.select_user(user_id)
            if user.status == 'admin':
                await message.answer('/add_words - Добавить слова\n\n'
                                     '/all - Получить все слова\n\n'
                                     '/delete - Удалить все слова\n\n'
                                     '/callback_with_user - Связь с пользователем\n\n'
                                     '/update_status - Поменять статус\n\n',
                                     )
            else:
                await message.answer('Вы не админ\n'
                                     'вам эти команды не доступны')

    except Exception:
        await message.answer('Error admins')


@dp.message_handler(IsPrivate(), commands=['callback_with_user'])
async def call_user_id(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            await message.answer('enter ID')
            await callback.callback_from_user.set()
        else:
            await message.answer("Извините, но эта функция доступна толко главному админу")

    except Exception:
        await message.answer('Error admins')


@dp.message_handler(state=callback.callback_from_user)
async def call_user_message(message: Message, state: FSMContext):
    try:
        answer = message.text
        await message.answer('enter text')
        await state.update_data(callback_from_user=answer)
        await callback.callback_text_user.set()

    except Exception:
        await state.finish()
        await message.answer('Error admins')


@dp.message_handler(state=callback.callback_text_user)
async def call_user_text(message: Message, state: FSMContext):
    try:
        answer = message.text
        data = await state.get_data()
        user_id = int(data.get('callback_from_user'))
        await bot.send_message(chat_id=user_id, text='السلام عليكم و رحمة الله و بركاته')
        await bot.send_message(chat_id=user_id, text=f'Сообщение от админа:\n\n'
                                                     f'{answer}')

    except Exception:
        await state.finish()
        await message.answer('Error admins')

    await state.finish()


@dp.message_handler(IsPrivate(), commands=['update_status'])
async def call_user_id(message: Message):
    try:
        user_id = message.from_user.id
        if user_id in admins_id:
            await message.answer('enter ID and new_status')
            await callback.update_status_user.set()
        else:
            await message.answer("Извините, но эта функция доступна толко главному админу")

    except Exception:
        await message.answer('Error admins')


@dp.message_handler(state=callback.update_status_user)
async def call_user_message(message: Message, state: FSMContext):
    try:
        user_id, answer = int(message.text.split()[0]), message.text.split()[1]
        await users_commands.update_status(user_id, answer)
        await message.answer('Статус успешно изменён')

    except Exception:
        await state.finish()
        await message.answer('Error admins')

    await state.finish()
