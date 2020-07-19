import psycopg2
from config import config


def fetchRegionOfImpact(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page-1)*20
    limit = 20

    cur.execute("""SELECT COUNT(impact_region_id) FROM region_of_impact_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM region_of_impact_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT impact_region, impact_region_id, status
            FROM region_of_impact_table ORDER BY impact_region_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"impact_region": row[0], "impact_region_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}
    
    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM region_of_impact_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT impact_region, impact_region_id, status
            FROM region_of_impact_table WHERE status='enabled' ORDER BY impact_region_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"impact_region": row[0], "impact_region_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    impact_region_id = requestParameters["impact_region_id"]

    cur.execute("""SELECT impact_region
           FROM region_of_impact_table
           WHERE impact_region_id= %(impact_region_id)s ;""", {"impact_region_id": impact_region_id})
    row = cur.fetchone()
    impact_region = row[0]

    return impact_region
