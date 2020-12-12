#!/usr/bin/python3
"""
contains the class definition of a City.
"""
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """
    Class to instance City objects. Link to cities table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
