from utils.db_api.schemas.db_word import MyWord
from utils.db_api.db_global import db
from asyncpg import UniqueViolationError
from random import sample, randint


async def add_word(user_id: int, word_id: int, word: str, translation: str, status: str):
    try:
        word = MyWord(user_id=user_id, word_id=word_id, word=word, translation=translation, status=status)
        await word.create()

    except UniqueViolationError:
        print("add word error")


async def select_myword(word_id):
    word = await MyWord.query.where(MyWord.word_id == word_id).gino.first()
    return word


async def count_words():
    count = await db.func.count(MyWord.word_id).gino.scalar()
    return count


async def update_status(word_id, new_status):
    word = await select_myword(word_id)
    await word.update(status=new_status).apply()


async def delete_word(user_id, word_id):
    words = await select_myword_all(user_id)
    for word in words:
        if word.word_id == word_id:
            await word.delete()
            return True
    return False


async def select_card(user_id):
    lis = await MyWord.query.where(MyWord.user_id == user_id).gino.all()
    lis_word = []
    for word in lis:
        if word.status == 'NO':
            lis_word.append(word)
    lis = lis_word.copy()
    lis_word.clear()
    return lis[randint(0, len(lis) - 1)]


async def select_myword_all(user_id):
    words = await MyWord.query.where(MyWord.user_id == user_id).gino.all()
    return words


async def select_all():
    lis = await MyWord.query.gino.all()
    lis_word = []
    for word in lis:
        lis_word.append(word.word_id)
    lis = lis_word.copy()
    lis_word.clear()
    if lis:
        word = max(lis)
        return word
    return 0


async def select_test(user_id):
    lis = await MyWord.query.where(MyWord.user_id == user_id).gino.all()
    lis_word = []
    for word in lis:
        if word.status == 'NO':
            lis_word.append(word)
    lis = lis_word.copy()
    lis_word.clear()
    word = lis[randint(0, len(lis)-1)]
    await update_status(word.word_id, 'retry')
    return word


async def generate_myword(user_id):
    try:
        words = await select_myword_all(user_id)
        lesson_words = []
        for word in words:
            if word.status != 'retry':
                lesson_words.append(word)
        words = lesson_words.copy()
        lesson_words.clear()
        if len(words)>= 3:
            return sample(words, 3)
        else:
            return False

    except Exception:
        return False


async def status_no(user_id):
    try:
        words = await select_myword_all(user_id)
        for word in words:
            await word.update(status='NO').apply()
    except Exception:
        return False