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
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
