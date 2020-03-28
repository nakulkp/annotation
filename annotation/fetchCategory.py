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
        FROM category_table
        WHERE status = 'enabled';""")
    rows = cur.fetchall()
    valueList = []
    i = 0
    for row in rows:
        value = {"categories": row[i][0], "category_id": row[i][1], "status": row[i][2]}
        valueList.append(value)
        i += 1

    cur.close()
    conn.commit()

    return {'valueList': valueList}
