import psycopg2
from annotation.config import config
from annotation.fetchCategory import fetchCategory


def fetchSubCategory(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']

    page = requestParameters['page']
    offset = (page-1)*20
    limit = 20

    cur.execute("""SELECT COUNT(sub_categories) FROM subcategory_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subcategory_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT sub_categories, sub_category_id, status, category_id
            FROM subcategory_table ORDER BY sub_category_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            if row[3] == None:
                value = {"sub_categories": row[0], "sub_category_id": row[1], "status": row[2], "category_id": row[3], "category": ""}
            else:
                value = {"sub_categories": row[0], "sub_category_id": row[1], "status": row[2], "category_id": row[3], "category": fetchCategory({'is_null' : "no", 'category_id':row[3], 'page': 0})}
            valueList.append(value)


        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subcategory_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT sub_categories, sub_category_id, status
            FROM subcategory_table WHERE status='enabled' ORDER BY sub_category_id ASC;""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"sub_categories": row[0], "sub_category_id": row[1], "status": row[2]}
            valueList.append(value)


        cur.close()
        conn.commit()

        return {'data': valueList}

    sub_category_id = requestParameters["sub_category_id"]

    cur.execute("""SELECT sub_categories
           FROM subcategory_table
           WHERE sub_category_id= %(sub_category_id)s ;""", {"sub_category_id": sub_category_id})
    row = cur.fetchone()
    sub_categories = row[0]

    return sub_categories
