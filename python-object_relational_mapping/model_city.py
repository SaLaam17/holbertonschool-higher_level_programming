#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class represents the 'cities' table in the database.

    Attributes:
        id (int): The city's unique identifier (Primary Key).
        name (str): The name of the city.
        state_id (int): The foreign key reference to the state's ID.

    Relationships:
        state (State): The state that this city belongs to.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")
