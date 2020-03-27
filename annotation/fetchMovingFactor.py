import psycopg2
from annotation.config import config


def fetchMovingFactor():
    conn = None
    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT moving_factors
        FROM moving_factor_table
        WHERE status = 'enabled';""")
    valueList = cur.fetchall()

    cur.close()
    conn.commit()

    return {'valueList': valueList}
    if conn is not None:
        conn.close()
