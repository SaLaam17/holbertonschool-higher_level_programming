#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Takes 3 arguments: MySQL username, MySQL password,
and database name and state name searched.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Establish the connection
    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=database
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY states.id ASC".format(state_name_searched))

    # Fetch all rows from the result of the query
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Don't forget to close the connection when done
    cur.close()
    conn.close()
