#!/usr/bin/python3
"""
Prints the State object with the name argument passed
from the database hbtn_0e_0_usa in ascending order by id

Usage:
    ./10-model_state_my_get.py <mysql_username> <mysql_password>
    <database_name> <state_name_searched>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name
    state_name_searched: State to filter

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    executes a query to retrieve all states ordered by `id`, and prints the
    first state.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = (
        session.query(State)
        .order_by(State.id)
        .filter(State.name == sys.argv[4])
        .all()
    )

    if states:
        for state in states:
            print(state.id)
    else:
        print("Not found")

    session.close()
