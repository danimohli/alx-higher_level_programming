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


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
