from utils.db_api.schemas.db_word import Word
from utils.db_api.db_global import db
from asyncpg import UniqueViolationError


async def add_word(word_id: int, level: int, lesson: int, word: str, translation: str):
    try:
        word = Word(word_id=word_id, level=level, lesson=lesson, word=word, translation=translation)
        await word.create()

    except UniqueViolationError:
        print("add word error")


async def select_word(word_id):
    word = await Word.query.where(Word.word_id == word_id).gino.first()
    return word


async def select_all():
    lis = await Word.query.gino.all()
    lis_word = []
    for word in lis:
        lis_word.append(word.word_id)
    lis = lis_word.copy()
    lis_word.clear()
    if lis:
        word = max(lis)
        return word
    return 0


async def select_lesson_words(level, lesson):
    level_words = await Word.query.where(Word.level == level).gino.all()
    lesson_words = []
    for word in level_words:
        if word.lesson == lesson:
            lesson_words.append(word)
    words = lesson_words.copy()
    lesson_words.clear()

    return words


async def count_words():
    count = await db.func.count(Word.word_id).gino.scalar()
    return count


async def update_word(word_id, new_word):
    word = await select_word(word_id)
    await word.update(word=new_word).apply()


async def update_translation(word_id, new_translation):
    word = await select_word(word_id)
    await word.update(translation=new_translation).apply()


async def delete_word(word_id):
    word = await select_word(word_id)
    await word.delete()
