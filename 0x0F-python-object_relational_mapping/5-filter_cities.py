#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities of that state,"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    """make a connection w our db"""
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    cur = db.cursor()
    cur.execute("SELECT id FROM states WHERE name=%s", stateName)

    res = cur.fetchonce()
    cur.execute("SELECT name FROM cities WHERE id=%s", )
