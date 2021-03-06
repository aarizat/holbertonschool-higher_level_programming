#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    with db.cursor() as cur:
        cur.execute('''SELECT * FROM states
                       ORDER BY id ASC''')
        [print(s) for s in cur.fetchall() if s[1].startswith('N')]
