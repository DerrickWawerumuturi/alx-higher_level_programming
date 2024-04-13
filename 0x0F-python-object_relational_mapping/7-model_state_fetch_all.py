#!/usr/bin/python3
"""script that lists all State objects from a database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")
    Session = sessionmaker(bind=engine)
    # instance of Session
    session = Session()

    results = session.query(State).order_by(State.id.asc()).all()
    for item in results:
        print(f"{item.id}: {item.name}")
