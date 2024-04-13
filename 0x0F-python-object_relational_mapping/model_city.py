#!/usr/bin/python3
"""file that contains the class definition of a City"""
from model_state import Base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey


class City(Base):
    """class City"""
    __tablename__ = "cities"
    id = (Column(Integer, autoincrement=True,
                 unique=True, nullable=False, primary_key=True))
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
