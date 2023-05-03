from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey

from db.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    first_name = Column(String)
    second_name = Column(String)
    is_admin = Column(Boolean)
