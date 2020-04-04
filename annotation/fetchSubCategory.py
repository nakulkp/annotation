import psycopg2
from annotation.config import config


def fetchSubCategory(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']
    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subcategory_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT sub_categories, sub_category_id, status
            FROM subcategory_table;""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"sub_categories": row[0], "sub_category_id": row[1], "status": row[2]}
            valueList.append(value)


        cur.close()
        conn.commit()

        return {'valueList': valueList}

    sub_category_id = requestParameters["sub_category_id"]

    cur.execute("""SELECT sub_categories
           FROM subcategory_table
           WHERE sub_category_id= %(sub_category_id)s ;""", {"sub_category_id": sub_category_id})
    row = cur.fetchone()
    sub_categories = row[0]

    return sub_categories
