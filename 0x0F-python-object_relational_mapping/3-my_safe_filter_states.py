#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE\
                    name LIKE BINARY %(name)s ORDER\
                    BY states.id ASC", {'name': argv[4]})
        states = cur.fetchall()
        for state in states:
            print(state)
    cur.close()
    db.close()
