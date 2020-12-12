#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    with db.cursor() as cur:
        cur.execute('''
                    SELECT cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    ON states.id = cities.state_id
                    ORDER BY cities.id ASC''')
        print(*[c for c, s in cur.fetchall() if s == sys.argv[4]], sep=', ')
