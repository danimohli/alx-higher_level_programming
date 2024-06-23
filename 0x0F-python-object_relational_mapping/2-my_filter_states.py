#!/usr/bin/python3
"""
Script to list states from the database
hbtn_0e_0_usa where name matches the argument, safe from SQL injections.

Usage:
    ./safe_list_states_with_name.py
    <username> <password> <database> <state_name>

Arguments:
    <username>: MySQL username
    <password>: MySQL password
    <database>: Database name
    <state_name>: State name to search for

Requirements:
    - Uses MySQLdb for database connectivity.
    - Connects to a MySQL server
    running on localhost at port 3306.
    - Lists states where name matches
    the argument in ascending order by id.
    - Results are displayed as (id, name) tuples.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
