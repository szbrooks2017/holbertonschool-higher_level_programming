#!usr/bin/python3
"""list all states from database hbtn_0e_0_usa"""

if __name__=="__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(argv[1], argv[2], argv[3])

    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    states = cur.fetchall()
    for state in states
        print(state)
    cur.close()
    db.close()

