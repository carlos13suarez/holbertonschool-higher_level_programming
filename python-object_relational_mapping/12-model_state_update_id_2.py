#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa where id = 2.

Usage:
    ./12-model_state_update_id_2.py <mysql_username> <mysql_password>
    <database_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    finds the State object with id = 2, changes its name to "New Mexico", and
    commits the change.
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

    state = (
        session.query(State)
        .filter(State.id == 2)
        .first()
    )
    state.name = 'New Mexico'
    session.commit()

    session.close()
