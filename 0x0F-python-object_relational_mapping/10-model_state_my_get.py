#!/usr/bin/python3
"""script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (session.query(State).filter(State.name == state_name).
              order_by(State.id.asc()).all())

    if (len(result) != 0):
        for state in result:
            print(state.id)
    else:
        print("Not found")
