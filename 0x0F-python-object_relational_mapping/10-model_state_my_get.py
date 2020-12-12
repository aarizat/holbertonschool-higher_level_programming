#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user, psswd, db, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, psswd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    state = Session().query(State).filter(State.name == name).first()
    print(state.id if state else 'Not found')
