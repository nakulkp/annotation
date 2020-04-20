import psycopg2
from annotation.config import config


def fetchCommodity(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page-1)*20
    limit = 20

    cur.execute("""SELECT COUNT(commodity_id) FROM commodity_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT commodities, commodity_id, status
            FROM commodity_table ORDER BY commodity_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"commodities": row[0], "commodity_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}
    
    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT commodities, commodity_id, status
            FROM commodity_table WHERE status='enabled' ORDER BY commodity_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"commodities": row[0], "commodity_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    commodity_id = requestParameters["commodity_id"]

    cur.execute("""SELECT commodities
           FROM commodity_table
           WHERE commodity_id= %(commodity_id)s ;""", {"commodity_id": commodity_id})
    row = cur.fetchone()
    commodities = row[0]

    return commodities
