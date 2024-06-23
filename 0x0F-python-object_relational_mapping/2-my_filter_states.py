#!/usr/bin/python3
"""
Script to list states from the database hbtn_0e_0_usa
where name matches the argument.

Usage:
    ./list_states_with_name.py <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name
    <state_name>: State name to search for

Requirements:
    - Uses MySQLdb for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Lists states where name matches the argument in ascending order by id.
    - Results are displayed as (id, name) tuples.
"""
import sys
import MySQLdb


def list_states_by_name(username, password, db_name, state_name):
    """
    Fetches and prints states from the database where name
    matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None
    """

    """
    Connect to Database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    """
    Order Queir
    """
    query = "SELECT id, name FROM states WHERE name = '{}'
    ORDER BY id ASC".format(state_name)

    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    list_states_by_name(username, password, db_name, state_name)
