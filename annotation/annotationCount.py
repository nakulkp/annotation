import psycopg2
from config import config


def annotationCount(requestPrameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)

    user_id = requestPrameters["user_id"]

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT COUNT(article_id)
        FROM master_table
        WHERE user_id = %(user_id)s;""", {"user_id": user_id})

    valueList = cur.fetchall()
    valueList = valueList[0]

    cur.close()
    conn.commit()
    conn.close()
    return {'count': valueList}
