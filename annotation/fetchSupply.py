import psycopg2
from annotation.config import config


def fetchSupply():
    conn = None
    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT supply_value
        FROM supply
        WHERE status = 'enabled';""")
    valueList = cur.fetchall()

    cur.close()
    conn.commit()

    return {'valueList': valueList}
    if conn is not None:
        conn.close()
