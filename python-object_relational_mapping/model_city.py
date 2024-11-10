#!/usr/bin/python3
"""
Defines a State class and an instance of Base = declarative_base().
Links to the MySQL table 'states'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class that links to the 'cities' table in a MySQL database.

    Attributes:
        id (int): The city's unique identifier, primary key, cannot be null.
        name (str): The city's name, cannot be null, max length 128 characters.
        state_id (int): Foreign key to the states table, cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
