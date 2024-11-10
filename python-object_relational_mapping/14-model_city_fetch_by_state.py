#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password>
    <database_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Database name

Description:
    This script connects to a MySQL server running on localhost at port 3306,
    retrieves all City objects sorted by cities.id in ascending order,
    and displays them in the format <state name>: (<city id>) <city name>.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City).\
        order_by(City.id).\
        all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
