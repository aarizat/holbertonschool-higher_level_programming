#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, psswd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = (session.query(State).filter(State.name.contains('a'))
              .order_by(State.id.asc()))

    for state in states:
        print('{}: {}'.format(state.id, state.name))
