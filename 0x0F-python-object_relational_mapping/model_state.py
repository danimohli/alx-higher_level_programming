#!/usr/bin/python3
"""
Contains the class definition of a State and
an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'.

    Attributes:
        id (int): Column of an auto-generated, unique integer,
        can't be null and is a primary key.
        name (str): Column of a string with maximum 128 characters
        and can't be null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
                           {password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
