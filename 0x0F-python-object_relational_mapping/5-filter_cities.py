#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id=states.id\
                WHERE states.name LIKE BINARY %(name)s ORDER BY cities.id\
                ASC", {'name': argv[4]})
        states = cur.fetchall()
    city = []
    for state in states:
        city.append(state[0])
    print(", ".join(city))
    cur.close()
    db.close()
