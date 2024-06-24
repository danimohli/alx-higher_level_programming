#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.

Usage:
    ./<script_name>.py <mysql_username> <mysql_password> <database_name>

Arguments:
    <mysql_username>: MySQL username
    <mysql_password>: MySQL password
    <database_name>: Name of the database

Requirements:
    - Uses SQLAlchemy for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Uses only one query to the database.
    - Uses the state relationship to access
    - the State object linked to the City object.
    - Results are sorted in ascending order by cities.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).
    join(City.state).order_by(City.id).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
