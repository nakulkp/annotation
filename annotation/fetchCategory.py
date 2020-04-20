import psycopg2
from annotation.config import config


def fetchCategory(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page-1)*20
    limit = 20

    cur.execute("""SELECT COUNT(category_id) FROM category_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM category_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT categories, category_id, status
            FROM category_table ORDER BY category_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"categories": row[0], "category_id": row[1], "status": row[2]}
            valueList.append(value)
        cur.close()
        conn.commit()
        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM category_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT categories, category_id, status
            FROM category_table WHERE status='enabled' ORDER BY category_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"categories": row[0], "category_id": row[1], "status": row[2]}
            valueList.append(value)
        cur.close()
        conn.commit()
        return {'data': valueList}

    category_id = requestParameters["category_id"]

    cur.execute("""SELECT categories
           FROM category_table
           WHERE category_id= %(category_id)s ;""", {"category_id": category_id})
    row = cur.fetchone()
    categories = row[0]

    return categories
