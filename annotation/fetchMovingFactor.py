import psycopg2
from annotation.config import config
from annotation.fetchCommodity import fetchCommodity
from annotation.fetchSubCategory import fetchSubCategory


def fetchMovingFactor(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page-1)*20
    limit = 20

    cur.execute("""SELECT COUNT(moving_factor_id) FROM moving_factor_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table ORDER BY moving_factor_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"moving_factors": row[0], "moving_factor_id": row[1], "status": row[2], "sub_category_id": row[3], "commodity_id": row[4], "sub_category" : fetchSubCategory({'is_null' : "no", 'sub_category_id': row[3], 'page': 0}),"commodity" : fetchCommodity({'is_null' : "no", 'commodity_id': row[4], 'page': 0}),}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT moving_factors, moving_factor_id, status
            FROM moving_factor_table WHERE status='enabled' ORDER BY moving_factor_id ASC;""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"moving_factors": row[0], "moving_factor_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    moving_factor_id = requestParameters["moving_factor_id"]

    cur.execute("""SELECT moving_factors
           FROM moving_factor_table
           WHERE moving_factor_id= %(moving_factor_id)s ;""",
                {"moving_factor_id": moving_factor_id})
    row = cur.fetchone()
    moving_factors = row[0]

    return moving_factors
