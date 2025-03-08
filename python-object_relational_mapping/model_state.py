#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """ State class to link to the 'states' table in the database """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
