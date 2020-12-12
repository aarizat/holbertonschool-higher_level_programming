#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, is safe from
MySQL injections!
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    with db.cursor() as cur:
        cur.execute('''
                    SELECT * FROM states
                    ORDER BY id ASC''')
        [print(s) for s in cur.fetchall() if s[1] == sys.argv[4]]
