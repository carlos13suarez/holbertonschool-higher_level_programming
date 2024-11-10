#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_0_usa
in ascending order by id

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password>
    <database_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    executes a query to retrieve all states ordered by `id`, and prints each
    state as a tuple in the format `(id, 'state_name')`.
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
