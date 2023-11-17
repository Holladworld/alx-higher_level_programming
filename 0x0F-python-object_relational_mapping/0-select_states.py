#!/usr/bin/python3
"""List states"""


import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    state = cursor.fetchall()

    for st in state:
        print(st)
