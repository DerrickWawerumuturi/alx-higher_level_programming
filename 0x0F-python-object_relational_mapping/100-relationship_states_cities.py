#!/usr/bin/python3
"""script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa:"""
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

    # create our tables
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    new_city = City(name="Nairobi", state_id=new_state.id)
    session.add(new_city)
    session.commit()
