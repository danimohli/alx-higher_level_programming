#!/usr/bin/python3
"""
All module comment
"""
import sys
import MySQLdb


def list_states_starting_with_N(username, password, db_name):
    """
    List all states with a name starting with 'N' from the database.
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
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states_starting_with_N(username, password, db_name)
