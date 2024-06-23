#!/usr/bin/python3
"""
Script to list states from the database hbtn_0e_0_usa starting with 'N'.

Usage:
    ./list_states_with_n.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Uses MySQLdb for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Lists states with names starting with 'N' in ascending order by id.
    - Results are displayed as (id, name) tuples.
"""

import sys
import MySQLdb


def list_states_starting_with_N(username, password, db_name):
    """
    Fetches and prints states from the database starting with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_states_with_n.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states_starting_with_N(username, password, db_name)
