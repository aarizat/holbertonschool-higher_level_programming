#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    with db.cursor() as cur:
        cur.execute('''
                    SELECT cities.id, cities.name, states.name
                    FROM cities, states
                    WHERE cities.state_id=states.id
                    ORDER BY cities.id ASC
                    ''')
        [print(s) for s in cur.fetchall()]
