#!/usr/bin/python3
"""
Script to list states from the database hbtn_0e_0_usa
where name matches the argume
"""
import sys
import MySQLdb


def list_states_by_name(username, password, db_name, state_name):
    """
    Fetches and prints states from the database where name
    matches
    """

    Connect to Database
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
