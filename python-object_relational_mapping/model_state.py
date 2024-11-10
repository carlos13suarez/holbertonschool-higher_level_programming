#!/usr/bin/python3
"""
Defines a State class and an instance of Base = declarative_base().
Links to the MySQL table 'states'.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    State class that links to the 'states' table in a MySQL database.

    Attributes:
        id (int): The state's unique identifier, primary key, cannot be null.
        name (str): The state's name, cannot be null, max length 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
