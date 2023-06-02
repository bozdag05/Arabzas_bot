from sqlalchemy import Column, BigInteger, String, Integer, sql

from utils.db_api.db_global import TimedBaseModel


class Word(TimedBaseModel):
    __tablename__ = 'word_arabic'

    word_id = Column(BigInteger, primary_key=True)
    word = Column(String(100))
    translation = Column(String(100))
    level = Column(Integer)
    lesson = Column(Integer)

    query: sql.select


class MyWord(TimedBaseModel):
    __tablename__ = 'my_word'

    user_id = Column(BigInteger, primary_key=True)
    word_id = Column(BigInteger, primary_key=True)
    word = Column(String(100))
    translation = Column(String(100))
    status = Column(String(30))
    query: sql.select


class RetryWord(TimedBaseModel):
    __tablename__ = 'retry_word'

    del_id = Column(Integer, primary_key=True)
    users_id = Column(BigInteger)
    retry_id = Column(Integer)
    status = Column(String(30))

    query: sql.select
