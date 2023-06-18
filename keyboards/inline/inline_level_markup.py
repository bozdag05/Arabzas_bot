from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


level_markup = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton('1', callback_data='level:1'),
                                            InlineKeyboardButton('2', callback_data='level:2'),
                                            InlineKeyboardButton('3', callback_data='level:3'),
                                            InlineKeyboardButton('4', callback_data='level:4'),
                                        ]
                                    ])

lesson_markup = InlineKeyboardMarkup(row_width=5,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton('1', callback_data='lesson:1'),
                                            InlineKeyboardButton('2', callback_data='lesson:2'),
                                            InlineKeyboardButton('3', callback_data='lesson:3'),
                                            InlineKeyboardButton('4', callback_data='lesson:4'),
                                            InlineKeyboardButton('5', callback_data='lesson:5'),
                                        ],
                                        [
                                            InlineKeyboardButton('6', callback_data='lesson:6'),
                                            InlineKeyboardButton('7', callback_data='lesson:7'),
                                            InlineKeyboardButton('8', callback_data='lesson:8'),
                                            InlineKeyboardButton('9', callback_data='lesson:9'),
                                            InlineKeyboardButton('10', callback_data='lesson:10'),
                                        ],
                                        [
                                            InlineKeyboardButton('11', callback_data='lesson:11'),
                                            InlineKeyboardButton('12', callback_data='lesson:12'),
                                            InlineKeyboardButton('13', callback_data='lesson:13'),
                                            InlineKeyboardButton('14', callback_data='lesson:14'),
                                            InlineKeyboardButton('15', callback_data='lesson:15'),
                                        ],
                                    ])