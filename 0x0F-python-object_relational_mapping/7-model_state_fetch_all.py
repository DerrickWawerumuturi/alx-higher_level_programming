#!/usr/bin/python3
"""script that prints the first State object from a database"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")

    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id.asc()).first()

    if res is not None:
        print(f"{res.id}: {res.name}")
    else:
        print("Nothing")
