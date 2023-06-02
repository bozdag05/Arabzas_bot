from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from states.state_test_1 import my_state
from keyboards.inline import again_mywrite_rus_ikb
from loader import dp, bot
from filters import IsPrivate
from utils.db_api import my_word_commands as my_commands
from keyboards.default import retry_class_word_kb as classes


@dp.callback_query_handler(text_contains='write_my_rus:start')
async def start_card(call: CallbackQuery, state: FSMContext):
    try:
        user_id = call.from_user.id
        await my_commands.status_no(user_id)
        word = await my_commands.select_card(user_id)

        await call.message.answer(f'___Переведите___\n')
        await call.message.answer(f'{word.translation}')
        await my_state.my_write_state_rus.set()
        await state.update_data(my_word_id_state=word.word_id)
    except Exception:
        await call.message.answer('Что-то не так')


@dp.message_handler(state=my_state.my_write_state_rus)
async def write_arab(message: Message, state: FSMContext):
    try:
        user_id, answer = message.from_user.id, message.text
        data = await state.get_data()
        word_id = int(data.get("my_word_id_state"))
        word = await my_commands.select_myword(word_id)

        if answer == '/end':
            await state.finish()
            await message.answer('Повторение завершено!', reply_markup=classes)
            return

        if word.word.lower() == answer.lower():
            await my_commands.update_status(word_id, 'YES')
            await message.answer('Правильно')
            word = await my_commands.select_card(user_id)
            await message.answer(f'___Переведите___\n')
            await message.answer(f'{word.translation}')
            await state.update_data(my_word_id_state=word.word_id)

        else:
            await message.answer('Не правильно')
            word = await my_commands.select_card(user_id)
            await message.answer(f'___Переведите___\n')
            await message.answer(f'{word.translation}')
            await state.update_data(my_word_id_state=word.word_id)


    except Exception:
        await state.finish()
        await message.answer(f"Вы завершили повторение урока\n\n"
                             f"повторить ещё раз ?", reply_markup=again_mywrite_rus_ikb)
