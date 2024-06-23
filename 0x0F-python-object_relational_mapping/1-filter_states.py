#!/usr/bin/python3
import sys
import MySQLdb
"""
modul to list state starting with letter N
"""


def list_states_starting_with_N(username, password, db_name):
    """
    List all states with a name starting with 'N' from the database.
    """
    
    """
    Connect to the database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """
    Create a cursor object
    """
    cur = db.cursor()

    """
    Execute the query to fetch states with names starting with 'N'
    ordered by id
    """
    cur.execute("SELECT id, name FROM states WHERE name
                LIKE 'N%' ORDER BY id ASC")

    """
    Fetch all the results
    """
    results = cur.fetchall()

    """
    Print the results
    """
    for row in results:
        print(row)

    """
    Close the cursor and the connection
    """
    cur.close()
    db.close()


if __name__ == "__main__":
    """
    Get arguments from command line
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """
    Call the function to list states
    """
    list_states_starting_with_N(username, password, db_name)
