#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    newState = State(name="Louisiana")
    session = Session()
    session.add(newState)
    session.commit()
    print(newState.id)
