#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.

Usage:
    ./list_cities_by_state.py <mysql_username>
    <mysql_password> <database_name> <state_name>

Arguments:
    <mysql_username>: MySQL username
    <mysql_password>: MySQL password
    <database_name>: Name of the database
    <state_name>: Name of the state to list cities for

Requirements:
    - Uses MySQLdb for database connectivity.
    - Connects to a MySQL server running on localhost at port 3306.
    - Lists cities in ascending order by cities.id.
    - Results are displayed as (id, name, state_name) tuples.
    - Ensures the query is safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)

    cur = db.cursor()
    """
    # Execute the query to fetch all cities of the given state
    """
    query = """SELECT cities.id, cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASi"""
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
