#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa in ascending order by id
with a name starting with N (upper N)

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    executes a query to retrieve all states ordered by `id`, and prints each
    state as a tuple in the format `(id, 'state_name')`.
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
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
