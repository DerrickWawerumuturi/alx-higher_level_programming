#!/usr/bin/python3
"""script that lists all cities from a database"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    """make a connection w our db"""
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    """cursor object"""
    cur = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
