async def on_startup(dp):

    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from utils.db_api.db_global import on_startup
    from loader import db

    '''print("Подключение к БД")
    await on_startup(dp)

    print("Удаляем таблицы в БД")
    await db.gino.drop_all()

    print("Создаём новые таблицы в БД")
    await db.gino.create_all()'''
    print("готово")

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print("Bot started")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
