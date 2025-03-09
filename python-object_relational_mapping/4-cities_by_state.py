#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_14_usa.
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

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        """)

    # Fetch all rows from the result of the query
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Don't forget to close the connection when done
    cur.close()
    conn.close()
