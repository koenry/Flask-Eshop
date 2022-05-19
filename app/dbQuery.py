import psycopg2
from pyrsistent import v


def databaseQuery(query):
    host = 'localhost'
    conn = psycopg2.connect(f" host={host} dbname=audimas user=postgres password=sa")
    cur = conn.cursor()
    cur.execute(query)
   
    if query.startswith("SELECT *"):
        a = cur.fetchall()
       
        return a
    elif query.startswith("PREPARE") or query.startswith("SELECT"):
        a = cur.fetchone()
        return a 
        # without return output everything will break as it will be null
    else:
        print('Query Success!')
    conn.commit()
    cur.close()
    conn.close()
    print('done')