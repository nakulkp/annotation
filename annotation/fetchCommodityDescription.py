import psycopg2
from config import config


def fetchCommodityDescription(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page - 1) * 20
    limit = 20

    cur.execute("""SELECT COUNT(comm_desc_id) FROM commodity_description_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0] // 20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_description_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT cd.comm_desc, cd.comm_desc_id, cd.status, c.commodities, c.commodity_id
            FROM commodity_description_table cd 
            INNER JOIN commodity_table c
            ON cd.commodity_id=c.commodity_id              
            ORDER BY cd.comm_desc_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"comm_desc": row[0], "comm_desc_id": row[1], "status": row[2], "commodities": row[3], "commodity_id": row[4]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_description_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT cd.comm_desc, cd.comm_desc_id, cd.status, c.commodities,c.commodity_id
            FROM commodity_description_table cd 
            INNER JOIN commodity_table c
            ON cd.commodity_id=c.commodity_id 
            WHERE cd.status='enabled' ORDER BY cd.comm_desc_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"comm_desc": row[0], "comm_desc_id": row[1], "status": row[2], "commodities": row[3], "commodity_id": row[4]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    comm_desc_id = requestParameters["comm_desc_id"]

    cur.execute("""SELECT cd.comm_desc
            FROM commodity_description_table cd 
            INNER JOIN commodity_table c
            ON cd.commodity_id=c.commodity_id 
           WHERE cd.comm_desc_id= %(comm_desc_id)s ;""", {"comm_desc_id": comm_desc_id})
    row = cur.fetchall()
    valueList = row[0]

    return valueList
