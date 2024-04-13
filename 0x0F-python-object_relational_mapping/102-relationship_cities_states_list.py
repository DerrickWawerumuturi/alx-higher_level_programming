#!/usr/bin/python3
"""
script that lists all City objects from
the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import declarative_base

Base = declarative_base()

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    # engine to connect to our db
    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")
    Session = sessionmaker(bind=engine)

    session = Session()
    res = session.query(City).order_by(City.id).all()

    for city in res:
        state = session.query(State).filter(city.state_id == State.id).first()
        print(f"{city.id}: {city.name} -> {state.name}")
