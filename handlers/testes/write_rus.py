from random import randint
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from states.state_test_1 import state_1
from keyboards.inline import again_write_rus_ikb
from loader import dp, bot
from filters import IsPrivate
from utils.db_api import retry_commands, word_commands as commands, users_commands, word_commands
from keyboards.default import retry_class_word_kb as classes


@dp.callback_query_handler(text_contains='write_rus:start')
async def start_card(call: CallbackQuery, state: FSMContext):

    try:
        user_id = call.from_user.id
        user = await users_commands.select_user(user_id)
        list_words = await commands.select_lesson_words(user.level, user.lesson)
        await retry_commands.delete_all(user_id)

        await retry_commands.add_words(user_id, list_words)
        retry_id = await retry_commands.select_retry_id(user_id)
        word = await commands.select_word(retry_id.retry_id)

        await call.message.answer(f'___Переведите___\n')
        await call.message.answer(f'{word.translation}')
        await state_1.write_state_rus.set()
        await state.update_data(del_id_state=retry_id.del_id)
        await state.update_data(word_id_state=word.word_id)
    except Exception:
        await call.message.answer('Что-то не так')


@dp.message_handler(state=state_1.write_state_rus)
async def write_arab(message: Message, state: FSMContext):

    try:
        user_id, answer = message.from_user.id, message.text
        data = await state.get_data()
        del_, word_id = int(data.get('del_id_state')), int(data.get("word_id_state"))
        word = await word_commands.select_word(word_id)

        if answer == '/end':
            await state.finish()
            await message.answer('Повторение завершено!', reply_markup=classes)
            return

        if word.word.lower() == answer.lower():
            await retry_commands.delete_retry_id(del_)
            await message.answer('Правильно')
            retry_id = await retry_commands.select_retry_id(user_id)
            word = await commands.select_word(retry_id.retry_id)
            await message.answer(f'___Переведите___\n')
            await message.answer(f'{word.translation}')
            await state.update_data(del_id_state=retry_id.del_id)
            await state.update_data(word_id_state=word.word_id)

        else:
            await message.answer('Не правильно')
            retry_id = await retry_commands.select_retry_id(user_id)
            word = await commands.select_word(retry_id.retry_id)
            await message.answer(f'___Переведите___\n')
            await message.answer(f'{word.translation}')
            await state.update_data(del_id_state=retry_id.del_id)
            await state.update_data(word_id_state=word.word_id)


    except Exception:
        await state.finish()
        await message.answer(f"Вы завершили повторение урока\n\n"
                             f"повторить ещё раз ?", reply_markup=again_write_rus_ikb)
