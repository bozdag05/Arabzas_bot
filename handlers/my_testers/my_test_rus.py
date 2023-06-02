import random
from random import randint
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from states.state_test_1 import my_state
from keyboards.inline import again_mytest_rus_ikb
from loader import dp, bot
from filters import IsPrivate
from utils.db_api import my_word_commands as my_commands, users_commands
from keyboards.default import retry_class_word_kb as classes
from utils.misc import rate_limit


@rate_limit(limit=3)
@dp.callback_query_handler(text_contains='test_my_rus:start')
async def start_card(call: CallbackQuery, state: FSMContext):

    try:
        user_id = call.from_user.id
        lis = []
        await my_commands.status_no(user_id)

        word = await my_commands.select_card(user_id)
        await my_commands.update_status(word.word_id, 'retry')
        words = await my_commands.generate_myword(user_id)
        if words != False:
            words.append(word)
            for i in words:
                word = await my_commands.select_myword(i.word_id)
                lis.append(word)
            random.shuffle(lis)
            test_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3,
                                      keyboard=[
                                          [
                                              KeyboardButton(f'{lis[0].word}'),
                                              KeyboardButton(f'{lis[1].word}'),
                                              KeyboardButton(f'{lis[2].word}'),
                                              KeyboardButton(f'{lis[3].word}'),
                                          ],
                                      ])
            lis.clear()
            await call.message.answer("Выберите правильный ответ:", reply_markup=test_kb)
            ans = await my_commands.select_myword(word.word_id)
            await call.message.answer(ans.translation)
            await my_state.my_test_state_rus.set()
            await state.update_data(my_word_id_state=word.word_id)
        else:
            await state.finish()
            await call.message.answer('Вы не можете создать и пройти тестирование\n'
                                  'У вас не достаточно слов в словаре')
    except Exception:
        await state.finish()
        await call.message.answer('Что-то не так')


@dp.message_handler(state=my_state.my_test_state_rus)
async def write_arab(message: Message, state: FSMContext):

    try:
        user_id, answer, lis = message.from_user.id, message.text, []
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
            await my_commands.update_status(word.word_id, 'retry')
            words = await my_commands.generate_myword(user_id)

            words.append(word)
            for i in words:
                word = await my_commands.select_myword(i.word_id)
                lis.append(word)
            random.shuffle(lis)
            test_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3,
                                          keyboard=[
                                              [
                                                  KeyboardButton(f'{lis[0].word}'),
                                                  KeyboardButton(f'{lis[1].word}'),
                                                  KeyboardButton(f'{lis[2].word}'),
                                                  KeyboardButton(f'{lis[3].word}'),
                                              ],
                                          ])
            lis.clear()
            await message.answer("Выберите правильный ответ:", reply_markup=test_kb)
            ans = await my_commands.select_myword(word.word_id)
            await message.answer(ans.translation)
            await my_state.my_test_state_rus.set()
            await state.update_data(my_word_id_state=word.word_id)

        else:
            await message.answer('Не правильно')
            await my_commands.update_status(word.word_id, 'NO')
            word = await my_commands.select_card(user_id)
            await my_commands.update_status(word.word_id, 'retry')
            words = await my_commands.generate_myword(user_id)

            words.append(word)
            for i in words:
                word = await my_commands.select_myword(i.word_id)
                lis.append(word)
            random.shuffle(lis)
            test_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3,
                                          keyboard=[
                                              [
                                                  KeyboardButton(f'{lis[0].word}'),
                                                  KeyboardButton(f'{lis[1].word}'),
                                                  KeyboardButton(f'{lis[2].word}'),
                                                  KeyboardButton(f'{lis[3].word}'),
                                              ],
                                          ])
            lis.clear()
            await message.answer("Выберите правильный ответ:", reply_markup=test_kb)
            ans = await my_commands.select_myword(word.word_id)
            await message.answer(ans.translation)
            await my_state.my_test_state_rus.set()
            await state.update_data(my_word_id_state=word.word_id)


    except Exception:
        await state.finish()
        await message.answer(f"Вы завершили повторение урока\n\n"
                             f"повторить ещё раз ?", reply_markup=again_mytest_rus_ikb)
