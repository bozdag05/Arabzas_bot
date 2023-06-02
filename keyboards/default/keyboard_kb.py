from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      keyboard=[
                                          [
                                              KeyboardButton('Добавить новое слово'),
                                              KeyboardButton('Удалить слово'),
                                          ],
                                          [
                                              KeyboardButton('Просмотр всех слов'),
                                              KeyboardButton('Узнать количество слов'),
                                          ],
                                      ])

retry_class_word_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                          keyboard=[
                                              [
                                                  KeyboardButton('Уроки'),
                                                  KeyboardButton('Свои слова')
                                              ]
                                          ])
