from aiogram.types import CallbackQuery
from keyboards.inline import again_card_arab_ikb
from loader import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.db_api import retry_commands, word_commands as commands, users_commands


@dp.callback_query_handler(text_contains='card_arab:start')
async def start_card(call: CallbackQuery):

    try:
        user_id = call.from_user.id
        user = await users_commands.select_user(user_id)
        list_words = await commands.select_lesson_words(user.level, user.lesson)
        await retry_commands.delete_all(user_id)
        await retry_commands.add_words(user_id, list_words)
        retry_id = await retry_commands.select_retry_id(user_id)
        word = await commands.select_word(retry_id.retry_id)
        ikb_1 = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[[InlineKeyboardButton(text=word.word,
                                                                            callback_data=f'card_arab:{word.translation}:{retry_id.del_id}')]])
        await call.message.answer('123456789_________Карточка_________123456789', reply_markup=ikb_1)
    except Exception:
        await call.message.answer('Что-то пошло не так')


@dp.callback_query_handler(text_contains='card_arab')
async def tester(call: CallbackQuery):

    try:
        user_id = call.from_user.id
        del_ = int(call.data.split(':')[2])
        ikb_1 = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text=call.data.split(':')[1], callback_data=f'none')]])
        await call.message.edit_reply_markup(ikb_1)
        await retry_commands.delete_retry_id(del_)

        retry_id = await retry_commands.select_retry_id(user_id)
        word = await commands.select_word(retry_id.retry_id)
        ikb_1 = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[[InlineKeyboardButton(text=word.word,
                                                                            callback_data=f'card_arab:{word.translation}:{retry_id.del_id}')]])
        await call.message.answer('_________Карточка_________', reply_markup=ikb_1)

    except Exception:
        await call.message.answer(f"Вы завершили повторение урока\n\n"
                                  f"повторить ещё раз ?", reply_markup=again_card_arab_ikb)
