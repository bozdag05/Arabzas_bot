from utils.db_api.schemas.db_user import User
from utils.db_api.db_global import db
from asyncpg import UniqueViolationError


async def add_user(user_id: int, first_name: str, last_name: str, level: int, lesson: int, status: str):

    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, level=level, lesson=lesson,
                    status=status)
        await user.create()

    except UniqueViolationError:
        print("add word error")


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def update_level(user_id, level):
    user = await select_user(user_id)

    await user.update(level=level).apply()


async def update_lesson(user_id, lesson):
    user = await select_user(user_id)
    await user.update(lesson=lesson).apply()


async def update_status(user_id, new_status):
    user = await select_user(user_id)
    await user.update(status=new_status).apply()