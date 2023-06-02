from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


retry_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Карточки арб/рус', callback_data='card_arab:start'),
                                          InlineKeyboardButton(text='Карточки рус/арб', callback_data='card_rus:start'),
                                      ],
                                      [
                                          InlineKeyboardButton(text='Тестирование арб/рус', callback_data='test_arab:start'),
                                          InlineKeyboardButton(text='Тестирование рус/арб', callback_data='test_rus:start'),
                                      ],
                                  ])

my_retry_ikb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Карточки арб/рус', callback_data='card_my_arab:start'),
                                          InlineKeyboardButton(text='Карточки рус/арб', callback_data='card_my_rus:start'),
                                      ],
                                      [
                                          InlineKeyboardButton(text='Тестирование арб/рус', callback_data='test_my_arab:start'),
                                          InlineKeyboardButton(text='Тестирование рус/арб', callback_data='test_my_rus:start'),
                                      ],
                                  ])
