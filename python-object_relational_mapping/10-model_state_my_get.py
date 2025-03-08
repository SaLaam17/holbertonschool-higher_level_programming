#!/usr/bin/python3
"""
Script that prints the State object
with the name passed as argument from the database.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_to_search = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://'
        '{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name_to_search).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
