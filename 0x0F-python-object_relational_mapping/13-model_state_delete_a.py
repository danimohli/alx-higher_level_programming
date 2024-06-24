#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./delete_states_with_a.py <mysql_username> <mysql_password> <database_name>

Arguments:
    <mysql_username>: MySQL username
    <mysql_password>: MySQL password
    <database_name>: Name of the database

Requirements:
    - Uses SQLAlchemy for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
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

    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
