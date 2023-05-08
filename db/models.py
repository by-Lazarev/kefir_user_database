from sqlalchemy import Column, Integer, String, Boolean

from db.database import Base


class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    first_name = Column(String)
    second_name = Column(String)
    other_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    city = Column(Integer)
    additional_info = Column(String)
    is_admin = Column(Boolean)
    password = Column(String)
