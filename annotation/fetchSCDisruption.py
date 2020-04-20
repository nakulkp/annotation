import psycopg2
from annotation.config import config


def fetchSCDisruption(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']
    page = requestParameters['page']
    offset = (page-1)*10
    limit = 10

    cur.execute("""SELECT COUNT(sc_disruption_value_id) FROM sc_disruption;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//10
    if (dataCount[0] % 10) != 0 and dataCount[0] > 10:
        pageCount = pageCount + 1

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM sc_disruption LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT sc_disruption_value, sc_disruption_value_id, status
            FROM sc_disruption LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"sc_disruption_value": row[0], "sc_disruption_value_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList, 'pages': pageCount}

    elif is_null == 'enabled':
        cur.execute("SELECT EXISTS (SELECT 1 FROM sc_disruption LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT sc_disruption_value, sc_disruption_value_id, status
            FROM sc_disruption WHERE status='enabled';""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"sc_disruption_value": row[0], "sc_disruption_value_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'data': valueList}

    sc_disruption_value_id = requestParameters["sc_disruption_value_id"]

    cur.execute("""SELECT sc_disruption_value
           FROM sc_disruption
           WHERE sc_disruption_value_id= %(sc_disruption_value_id)s ;""", {"sc_disruption_value_id": sc_disruption_value_id})
    row = cur.fetchone()
    sc_disruption_value = row[0]

    return sc_disruption_value
