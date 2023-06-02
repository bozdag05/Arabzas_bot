import random
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from states.state_test_1 import state_1
from keyboards.inline import again_test_arab_ikb
from loader import dp, bot
from keyboards.default import retry_class_word_kb as classes
from utils.db_api import retry_commands, word_commands as commands, users_commands, word_commands


@dp.callback_query_handler(text_contains='test_rus:start')
async def start_card(call: CallbackQuery, state: FSMContext):

    try:
        user_id = call.from_user.id
        lis = []
        user = await users_commands.select_user(user_id)
        list_words = await commands.select_lesson_words(user.level, user.lesson)
        await retry_commands.delete_all(user_id)
        await retry_commands.add_words(user_id, list_words)
        retry_id = await retry_commands.select_retry_test_id(user_id)
        await retry_commands.update_status(retry_id.del_id, 'retry')
        words = await retry_commands.generate_word(user_id)

        if words != False:
            words.append(retry_id)
            for i in words:
                word = await commands.select_word(i.retry_id)
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
            ans = await word_commands.select_word(retry_id.retry_id)
            await call.message.answer(ans.translation)
            await state_1.test_state_rus.set()
            await state.update_data(del_id_state=retry_id.del_id)
            await state.update_data(word_id_state=retry_id.retry_id)
        else:
            await state.finish()
            await call.message.answer('Вы не можете создать и пройти тестирование\n'
                                  'У вас не достаточно слов в словаре')
    except Exception:
        await state.finish()
        await call.message.answer('Что-то не так')


@dp.message_handler(state=state_1.test_state_rus)
async def write_arab(message: Message, state: FSMContext):

    try:
        user_id, answer, lis = message.from_user.id, message.text, []
        data = await state.get_data()
        del_, word_id = int(data.get('del_id_state')), int(data.get("word_id_state"))
        word = await word_commands.select_word(word_id)

        if answer == '/end':
            await state.finish()
            await message.answer('Повторение завершено!', reply_markup=classes)
            return

        elif word.word.lower() == answer.lower():
            await retry_commands.update_status(del_, 'YES')
            await message.answer('Правильно')
            retry_id = await retry_commands.select_retry_test_id(user_id)
            await retry_commands.update_status(retry_id.del_id, 'retry')
            words = await retry_commands.generate_word(user_id)
            words.append(retry_id)
            for i in words:
                word = await commands.select_word(i.retry_id)
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
            ans = await word_commands.select_word(retry_id.retry_id)
            await message.answer(ans.translation)
            await state_1.test_state_rus.set()
            await state.update_data(del_id_state=retry_id.del_id)
            await state.update_data(word_id_state=retry_id.retry_id)

        else:
            await message.answer('Не правильно')
            await retry_commands.update_status(del_, 'NO')
            retry_id = await retry_commands.select_retry_test_id(user_id)
            await retry_commands.update_status(retry_id.del_id, 'retry')
            words = await retry_commands.generate_word(user_id)
            words.append(retry_id)
            for i in words:
                word = await commands.select_word(i.retry_id)
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
            ans = await word_commands.select_word(retry_id.retry_id)
            await message.answer(ans.translation)
            await state_1.test_state_rus.set()
            await state.update_data(del_id_state=retry_id.del_id)
            await state.update_data(word_id_state=retry_id.retry_id)

    except Exception:
        await state.finish()
        await message.answer(f"Вы завершили повторение урока\n\n"
                             f"повторить ещё раз ?", reply_markup=again_test_arab_ikb)
