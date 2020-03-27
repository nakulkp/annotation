import psycopg2
from annotation.config import config


def fetchSCDisruption():
    conn = None
    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT sc_disruption_value
        FROM sc_disruption
        WHERE status = 'enabled';""")
    valueList = cur.fetchall()

    cur.close()
    conn.commit()

    return {'valueList': valueList}
    if conn is not None:
        conn.close()
