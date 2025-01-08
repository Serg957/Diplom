from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean# ForeignKey позволяет указать на другую ячейку и произвести связь между таблицами
from sqlalchemy.orm import relationship
from models import *



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')


