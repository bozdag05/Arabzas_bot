from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


again_mycard_rus_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='card_my_rus:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='my_end:'),
                                      ]
                                  ])

again_mycard_arab_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='card_my_arab:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='my_end:'),
                                      ]
                                  ])

again_mywrite_arab_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='write_my_arab:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='my_end:'),
                                      ]
                                  ])

again_mywrite_rus_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='write_my_rus:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='my_end:'),
                                      ]
                                  ])

again_mytest_arab_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='test_my_arab:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='my_end:'),
                                      ]
                                  ])

again_mytest_rus_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Повторить ещё раз?', callback_data='test_my_rus:start'),
                                          InlineKeyboardButton(text='Завершить', callback_data='my_end:'),
                                      ]
                                  ])
