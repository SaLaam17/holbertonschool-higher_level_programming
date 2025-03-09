#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_14_usa.
Your script should take 4 arguments:
mysql username, mysql password,
database name and state name
(SQL injection free!)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command line arguments.
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Establish the connection.
    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=database
    )

    # Create a cursor object to interact with the database.
    cur = conn.cursor()

    # Use a parameterized query to avoid SQL injection.
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all rows from the result of the query
    rows = cur.fetchall()

    # Prepare the list of cities
    cities = [row[0] for row in rows]

    # Print the cities separated by commas
    print(", ".join(cities))

    # Close the connection when done.
    cur.close()
    conn.close()
