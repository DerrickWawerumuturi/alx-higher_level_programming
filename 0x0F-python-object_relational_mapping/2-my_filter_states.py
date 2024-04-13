#!/usr/bin/python3
"""script that takes in an argument and displays
all values in the states table """
if __name__ == "__main__":
    import sys
    import MySQLdb

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    """make the connection"""
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)
    query = "SELECT * FROM states WHERE states.name= BINARY'{}' \
        ORDER BY states.id ASC".format(stateName)

    cur = db.cursor()
    """execute query"""
    cur.execute(query)
    """get results"""
    rows = cur.fetchall()
    """rows will be a list of tuples"""
    for row in rows:
        print(row)
    cur.close()
    db.close()
