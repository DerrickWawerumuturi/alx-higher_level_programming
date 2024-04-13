#!/usr/bin/python3
"""script that lists all states from a database"""
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
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    """get result of previous execution"""
    rows = cur.fetchall()
    """rows will be a list of tuples"""
    for row in rows:
        print(row)
    cur.close()
    db.close()
