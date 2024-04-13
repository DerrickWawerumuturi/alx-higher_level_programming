#!/usr/bin/python3
"""List all State objects with letter a"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")

    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id.asc())

    for state in results:
        print(f"{state.id}: {state.name}")
