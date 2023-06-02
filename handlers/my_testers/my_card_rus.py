from aiogram.types import CallbackQuery
from keyboards.inline import again_mycard_rus_ikb
from loader import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import my_word_commands as my_commands


@dp.callback_query_handler(text_contains='card_my_rus:start')
async def start_card(call: CallbackQuery):

    try:
        user_id = call.from_user.id
        await my_commands.status_no(user_id)

        word = await my_commands.select_card(user_id)
        ikb_1 = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[[InlineKeyboardButton(text=word.translation,
                                                                        callback_data=f'card_my_rus:{word.word}:{word.word_id}')]])
        await call.message.answer('_________Карточка_________', reply_markup=ikb_1)

    except Exception:
        await call.message.answer('Что-то не так')


@dp.callback_query_handler(text_contains='card_my_rus')
async def tester(call: CallbackQuery):

    try:
        user_id = call.from_user.id
        ikb_1 = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text=call.data.split(':')[1], callback_data=f'none')]])
        await call.message.edit_reply_markup(ikb_1)
        word_id = int(call.data.split(':')[2])
        await my_commands.update_status(word_id, 'YES')
        word = await my_commands.select_card(user_id)

        ikb_1 = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[[InlineKeyboardButton(text=word.translation,
                                                                            callback_data=f'card_my_rus:{word.word}:{word.word_id}')]])
        await call.message.answer('_________Карточка_________', reply_markup=ikb_1)

    except Exception:
        await call.message.answer(f"Вы завершили повторение урока\n\n"
                                  f"повторить ещё раз ?", reply_markup=again_mycard_rus_ikb)
