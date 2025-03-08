#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://'
        '{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
