from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base


class PeopleDb(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, index=True)
    lname = Column(String(100), nullable=False, unique=True)
    fname = Column(String(100), nullable=False, unique=False)
    timestamp = Column(Date, nullable=False, unique=False)