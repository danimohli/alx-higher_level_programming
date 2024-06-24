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

if __name__ == "__main__":
    from sqlalchemy.engine import create_engine
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import Session
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv

    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': argv[1],
          'password': argv[2],
          'database': argv[3]}

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
