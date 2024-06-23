#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.

Usage:
    ./list_cities.py <username> <password> <database>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name

Requirements:
    - Uses MySQLdb for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Lists cities in ascending order by cities.id.
    - Results are displayed as (id, name) tuples.
"""
import sys
import MySQLdb


def list_cities(username, password, db_name):
    """
    Fetches and prints all cities from the database.

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

    cur.execute("SELECT id, name FROM cities ORDER BY id ASC")

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities(username, password, db_name)
