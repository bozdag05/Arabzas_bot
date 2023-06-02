import random

from utils.db_api.schemas.db_word import RetryWord
from utils.db_api.db_global import db
from asyncpg import UniqueViolationError
from random import randint


async def add_words(users_id: int, list_id):
    for word in list_id:
        try:
            retry = RetryWord(users_id=users_id, retry_id=word.word_id, status='NO')
            await retry.create()

        except UniqueViolationError:
            print("add word error")


async def select_retry_id(users_id):
    lis = await RetryWord.query.where(RetryWord.users_id == users_id).gino.all()
    return lis[randint(0, len(lis)-1)]


async def select_retry_test_id(users_id):
    lis = await RetryWord.query.where(RetryWord.users_id == users_id).gino.all()
    lis_word = []
    for word in lis:
        if word.status == 'NO':
            lis_word.append(word)
    lis = lis_word.copy()
    lis_word.clear()
    return lis[randint(0, len(lis)-1)]


async def select_retry_all(users_id):
    lis = await RetryWord.query.where(RetryWord.users_id == users_id).gino.all()
    return lis


async def select_delete_id(del_id):
    id = await RetryWord.query.where(RetryWord.del_id == del_id).gino.first()
    return id


async def delete_retry_id(del_id):
    word = await select_delete_id(del_id)
    await word.delete()


async def delete_all(users_id):
    try:
        words = await select_retry_all(users_id)
        for w in words:
            word = await select_delete_id(w.del_id)
            await word.delete()
    except Exception:
        return


async def generate_word(users_id):
    try:
        words = await select_retry_all(users_id)
        lesson_words = []
        for word in words:
            if word.status != 'retry':
                lesson_words.append(word)
        words = lesson_words.copy()
        lesson_words.clear()
        if len(words)>= 3:
            return random.sample(words, 3)
        else:
            return False

    except Exception:
        return False


async def update_status(del_id, new_status):
    word = await RetryWord.query.where(RetryWord.del_id == del_id).gino.first()
    await word.update(status=new_status).apply()