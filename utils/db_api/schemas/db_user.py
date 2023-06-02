from sqlalchemy import Column, String, BigInteger, Integer, sql

from utils.db_api.db_global import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'user'

    user_id = Column(BigInteger, primary_key=True)
    level = Column(Integer)
    lesson = Column(Integer)
    first_name = Column(String(100))
    last_name = Column(String(100))
    status = Column(String(30))

    query: sql.select