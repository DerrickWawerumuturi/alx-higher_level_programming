#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    """connect w our database"""
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    cur = db.cursor()
    """execute our query"""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
