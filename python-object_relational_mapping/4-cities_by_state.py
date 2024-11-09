#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa in ascending order by id

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    executes a query to retrieve all states ordered by `cities.id`, and prints
    each state as a tuple in the format `(cities.id, 'cities.name',
    'state.name')`.
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
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM states, cities "
                "WHERE cities.state_id = states.id "
                "ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
