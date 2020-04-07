import psycopg2
from annotation.config import config


def fetchSupply(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']

    page = requestParameters['page']
    offset = (page-1)*10
    limit = offset + 10

    cur.execute("""SELECT COUNT(category_id) FROM category_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//10
    if (dataCount[0] % 10) != 0:
        pageCount = pageCount + 1
        
    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM supply LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT supply_value, supply_value_id, status
            FROM supply WHERE status='enabled';""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"supply_value": row[0], "supply_value_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    supply_value_id = requestParameters["supply_value_id"]

    cur.execute("""SELECT supply_value
           FROM supply
           WHERE supply_value_id= %(supply_value_id)s ;""", {"supply_value_id": supply_value_id})
    row = cur.fetchone()
    supply_value = row[0]

    return supply_value
