#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage:
    ./first_state.py <mysql_username> <mysql_password> <database_name>

Arguments:
    <mysql_username>: MySQL username
    <mysql_password>: MySQL password
    <database_name>: Name of the database

Requirements:
    - Uses SQLAlchemy for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Displays the first State in ascending order by states.id.
    - If the table states is empty, prints "Nothing" followed by a new line.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
                           {password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()
