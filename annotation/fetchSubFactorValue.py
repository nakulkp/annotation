import psycopg2
from config import config


def fetchSubFactorValue(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page - 1) * 20
    limit = 20

    cur.execute("""SELECT COUNT(subfactorvalue_id) FROM subfactorvalue_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0] // 20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subfactorvalue_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT subfactorvalue, subfactorvalue_id, status
            FROM subfactorvalue_table ORDER BY subfactorvalue_id ASC LIMIT %(limit)s OFFSET %(offset)s;""",
                    {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"subfactorvalue": row[0], "subfactorvalue_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subfactorvalue_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT subfactorvalue, subfactorvalue_id, status
            FROM subfactorvalue_table WHERE status='enabled' ORDER BY subfactorvalue_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"subfactorvalue": row[0], "subfactorvalue_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    subfactorvalue_id = requestParameters["subfactorvalue_id"]

    cur.execute("""SELECT subfactorvalue
           FROM subfactorvalue_table
           WHERE subfactorvalue_id= %(subfactorvalue_id)s ;""", {"subfactorvalue_id": subfactorvalue_id})
    row = cur.fetchone()
    subfactorvalue = row[0]

    return subfactorvalue
