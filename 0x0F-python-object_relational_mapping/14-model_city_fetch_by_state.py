#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user, psswd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, psswd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(City.state_id == State.id).all()

    for s, c in cities:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
