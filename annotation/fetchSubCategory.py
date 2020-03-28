import psycopg2
from annotation.config import config


def fetchSubCategory():
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM subcategory_table LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT sub_categories, sub_category_id, status
        FROM subcategory_table
        WHERE status = 'enabled';""")
    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"sub_categories": row[0], "sub_category_id": row[1], "status": row[2]}
        valueList.append(value)


    cur.close()
    conn.commit()

    return {'valueList': valueList}
    if conn is not None:
        conn.close()
