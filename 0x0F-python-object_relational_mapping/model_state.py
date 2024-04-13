#!/usr/bin/python3
"""file that contains the class definition of a
State and an instance Base = declarative_base()"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""class State that inherits from Base"""


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ :name of the MySQL table to store States.
    id: state's id.
    name: state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
