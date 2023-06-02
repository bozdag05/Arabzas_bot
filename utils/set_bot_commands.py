from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запуск бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('type_tests', 'Виды тестов'),
        types.BotCommand('menu_user', 'Меню для работы с словарём'),
        types.BotCommand('info', 'Информация о боте'),
        types.BotCommand('callback', 'Обратная связь с админом'),
        types.BotCommand('end', 'Завершить тест'),
        types.BotCommand('get_admins_commands', 'Команды админа'),
    ])

