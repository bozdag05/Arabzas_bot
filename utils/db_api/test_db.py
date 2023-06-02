import asyncio

from data import config
from loader import db
from utils.db_api import retry_commands as commands
from utils.db_api import word_commands as word_command
from random import randint


async def test():

    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await word_command.add_word(
        word_id=1,
        lesson=1,
        level=1,
        word='word1',
        translation='translation1'
    )
    await word_command.add_word(
        word_id=2,
        lesson=1,
        level=1,
        word='word2',
        translation='translation2'
    )
    await word_command.add_word(
        word_id=3,
        lesson=1,
        level=1,
        word='word3',
        translation='translation3'
    )
    lis = await word_command.select_lesson_words(1, 1)

    await commands.add_words(228, lis)

    id = await commands.select_retry_id(228)
    retry_word = await word_command.select_word(id.retry_id)
    word = id.del_id
    print(word, id)


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
