#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa in ascending order
by cities.id.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name
    state_name: State to filter cities by

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    executes a query to retrieve all cities of a given state ordered by
    `cities.id`, and prints the result as a comma-separated list of city names.
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
    cur.execute("SELECT cities.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(*city_names, sep=', ')

    cur.close()
    db.close()
