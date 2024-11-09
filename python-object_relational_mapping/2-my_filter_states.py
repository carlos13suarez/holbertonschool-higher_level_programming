#!/usr/bin/python3
"""
Takes in state argument from the user and displays the values where name
matches the argument in ascending order by id

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>
    <state_name_searched>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name
    state_name_searched: State to filter

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    executes a query to retrieve all states where `name` matches, and prints
    each state as a tuple in the format `(id, 'state_name')`.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main entrance
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE BINARY name LIKE %s "
                "ORDER BY id ASC", (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
