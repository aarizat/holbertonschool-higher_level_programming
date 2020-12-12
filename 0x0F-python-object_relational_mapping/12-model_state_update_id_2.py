#!/usr/bin/python3
"""
changes the name of a State object from the database
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, psswd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
