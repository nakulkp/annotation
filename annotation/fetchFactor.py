import psycopg2
from config import config


def fetchFactor(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page-1)*20
    limit = 20

    cur.execute("""SELECT COUNT(factor_id) FROM factor_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM factor_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT factor, factor_id, status
            FROM factor_table ORDER BY factor_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"factor": row[0], "factor_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}
    
    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM factor_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT factor, factor_id, status
            FROM factor_table WHERE status='enabled' ORDER BY factor_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"factor": row[0], "factor_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    factor_id = requestParameters["factor_id"]

    cur.execute("""SELECT factor
           FROM factor_table
           WHERE factor_id= %(factor_id)s ;""", {"factor_id": factor_id})
    row = cur.fetchone()
    factor = row[0]

    return factor
