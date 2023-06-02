from aiogram.dispatcher import FSMContext

from keyboards.default import menu_kb
from utils.db_api import my_word_commands as commands
from loader import dp
from aiogram.types import Message
from states.state_test_1 import user_state


@dp.message_handler(text='Просмотр всех слов')
async def add_word(message: Message):

    try:
        user_id = message.from_user.id
        words = await commands.select_myword_all(user_id)
        if words == []:
            await message.answer('В вашем славаре нет слов')
            return

        for word in words:
            await message.answer(f'ID: {word.word_id}\n\n'
                                f'Слово: {word.word}\n'
                                f'Перевод: {word.translation}')
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(text='Узнать количество слов')
async def add_word(message: Message):

    try:
        user_id = message.from_user.id
        count_words = await commands.select_myword_all(user_id)
        await message.answer(f'Количество ваших слов: {len(count_words)}')

    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(text='Добавить новое слово')
async def add_word(message: Message):
    try:
        await message.answer('Введите новое слово')
        await user_state.add_word_state.set()

    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(state=user_state.add_word_state)
async def add_translation(message: Message, state: FSMContext):

    try:
        answer = message.text
        await state.update_data(add_word_state=answer)
        await message.answer('Введите перевод')
        await user_state.add_translation_state.set()

    except Exception:
        await state.finish()
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(state=user_state.add_translation_state)
async def save_word(message: Message, state: FSMContext):

    try:
        answer, user_id = message.text, message.from_user.id
        await state.update_data(add_translation_state=answer)
        word_id = await commands.select_all()
        data = await state.get_data()
        word, translation = data.get('add_word_state'), data.get('add_translation_state')
        await commands.add_word(
            user_id=user_id,
            word_id=word_id+1,
            word=word.lower(),
            translation=translation.lower(),
            status='NO'
        )

        await message.answer('Проверьте всё ли корректно заполнено')
        word = await commands.select_myword(word_id+1)
        await message.answer(f'ID: {word.word_id}\n\n'
                            f'Новое слово: {word.word}\n'
                            f'Перевод: {word.translation}')

        await message.answer('Добавить ещё ?', reply_markup=menu_kb)
        await state.finish()

    except Exception:
        await state.finish()
        await message.answer('Что-то не так, попробуйте ещё раз')

    await state.finish()


@dp.message_handler(text='Удалить слово')
async def del_word(message: Message):
    try:
        await message.answer('Введите ID слово, которе хотите удалить')
        await user_state.get_id_state.set()
    except Exception:
        await message.answer('Что-то не так, попробуйте ещё раз')


@dp.message_handler(state=user_state.get_id_state)
async def del_word(message: Message, state: FSMContext):

    try:
        user_id, answer = message.from_user.id, int(message.text)

        res = await commands.delete_word(user_id, answer)
        if res != False:
            await message.answer('слово успешно удалено', reply_markup=menu_kb)
        else:
            await message.answer('Некорректный ввод')

        await state.finish()

    except Exception:
        await state.finish()
        await message.answer('Некорректный ввод')

    await state.finish()