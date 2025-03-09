#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: MySQL username, MySQL password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish the connection
    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=database
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows from the result of the query
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Don't forget to close the connection when done
    cur.close()
    conn.close()
