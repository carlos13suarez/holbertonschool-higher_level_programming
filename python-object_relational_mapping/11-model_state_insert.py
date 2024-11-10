#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.

Usage:
    ./11-model_state_insert.py <mysql_username> <mysql_password>
    <database_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    adds a new State object with the name “Louisiana”, and prints the new State id.
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

    lousiana_state = State(name='Louisiana')
    session.add(lousiana_state)
    session.commit()

    print(lousiana_state.id)

    session.close()
