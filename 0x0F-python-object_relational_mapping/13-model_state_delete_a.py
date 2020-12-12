#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa
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
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()
