#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.

Arguments:
    mysql_username (str): MySQL username.
    mysql_password (str): MySQL password.
    database_name (str): Name of the database.

It connects to a MySQL database using SQLAlchemy, fetches all cities,
and displays them ordered by city ID, with the format:
    <state name>: (<city id>) <city name>
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
import sys

if len(sys.argv) < 4:
    print("Usage: python3 14-model_city_fetch_by_state.py\
          <mysql_username> <mysql_password> <database_name>")
    sys.exit(1)

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
