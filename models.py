from gino import Gino
from typing import List
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, Table, DateTime, BigInteger, sql
from datetime import datetime


db = Gino()

class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.primary_key.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"



class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True)
    username = Column(String(100))
    balance = Column(Integer, default=0)
    connection_date = Column(DateTime, default=datetime.utcnow())

    query: sql.Select
