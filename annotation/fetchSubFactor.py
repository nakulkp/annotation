import psycopg2
from config import config


def fetchSubFactor(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page - 1) * 20
    limit = 20

    cur.execute("""SELECT COUNT(subfactor_id) 
    FROM subfactor_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0] // 20
    if (dataCount[0] % 20) != 0 and dataCount[0] > 20:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subfactor_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT s.subfactor, s.subfactor_id, s.status, f.factor
            FROM subfactor_table s 
            INNER JOIN factor_table f 
            ON s.factor_id=f.factor_id 
            ORDER BY s.subfactor_id ASC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"subfactor": row[0], "subfactor_id": row[1], "status": row[2], "factor": row[3]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM subfactor_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT s.subfactor, s.subfactor_id, s.status, f.factor
            FROM subfactor_table s 
            INNER JOIN factor_table f ON s.factor_id=f.factor_id
            WHERE s.status='enabled' 
            ORDER BY s.subfactor_id ASC;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"subfactor": row[0], "subfactor_id": row[1], "status": row[2], "factor": row[3]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    subfactor_id = requestParameters["subfactor_id"]

    cur.execute("""SELECT s.subfactor, f.factor
           FROM subfactor_table s 
           INNER JOIN factor_table f 
           ON s.factor_id=f.factor_id
           WHERE subfactor_id= %(subfactor_id)s ;""", {"subfactor_id": subfactor_id})
    rows = cur.fetchall()
    valueList = []
    for row in rows:
        value = {"subfactor": row[0], "factor": row[1]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'data': valueList}
