#!/usr/bin/python3
"""Update state object"""

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

    state = session.query(State).filter(State.id == '2').first()

    state.name = 'New Mexico'

    session.commit()
