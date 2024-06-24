#!/usr/bin/python3
"""
Creates the State “California” with the City
“San Francisco” in the database hbtn_0e_100_usa.

Usage:
    ./100-relationship_states_cities.py
    <mysql_username> <mysql_password> <database_name>

Arguments:
    <mysql_username>: MySQL username
    <mysql_password>: MySQL password
    <database_name>: Name of the database

Requirements:
    - Uses SQLAlchemy for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Uses the cities relationship for all State objects.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{db_name}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.add(new_city)

    session.commit()

    session.close()
