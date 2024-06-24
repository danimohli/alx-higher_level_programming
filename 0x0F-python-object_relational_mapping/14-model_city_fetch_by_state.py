#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username>
    <mysql_password> <database_name>

Arguments:
    <mysql_username>: MySQL username
    <mysql_password>: MySQL password
    <database_name>: Name of the database

Requirements:
    - Uses SQLAlchemy for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Results must be sorted in ascending order by cities.id.
    - Results must be displayed as <state name>: (<city id>) <city name>.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
