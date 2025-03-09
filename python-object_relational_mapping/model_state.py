#!/usr/bin/python3
"""
Start link class to table in database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class represents the 'states' table in the database.

    Attributes:
        id (int): The state's unique identifier (Primary Key).
        name (str): The name of the state.

    Relationships:
        cities (list): List of City objects related to this state.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
