#!/usr/bin/python3
"""
contains the class definition of a State and an instance
Base = declarative_base()
"""
import sys
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


user, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(user, psswd, db), pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    """
    Class to create state objects. Link to table states.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
