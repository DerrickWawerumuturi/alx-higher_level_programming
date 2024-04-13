#!/usr/bin/python3
"""script that that prints all City objects
from the database hbtn_0e_14_usa"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City).order_by(City.id).all()

    for city in res:
        state_name = (session.query(State).
                      filter(city.state_id == State.id).first())
        print(f"{state_name.name}: ({city.id}) {city.name}")
