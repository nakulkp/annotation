import psycopg2
from annotation.config import config


def fetchCategory():
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM category_table LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT categories, category_id, status
        FROM category_table;""")
    rows = cur.fetchall()
    valueList = []
    for row in rows:
        value = {"categories": row[0], "category_id": row[1], "status": row[2]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'valueList': valueList}
