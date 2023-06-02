from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


again_card_rus_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='card_rus:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='end:card_rus'),
                                      ]
                                  ])

again_card_arab_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='card_arab:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='end:card_arab'),
                                      ]
                                  ])

again_write_arab_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='write_arab:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='end:write_arab'),
                                      ]
                                  ])

again_write_rus_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='write_rus:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='end:write_rus'),
                                      ]
                                  ])

again_test_arab_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='test_arab:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='end:test_arab'),
                                      ]
                                  ])

again_test_rus_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='test_rus:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='end:rus_arab'),
                                      ]
                                  ])