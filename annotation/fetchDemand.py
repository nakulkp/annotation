import psycopg2
from annotation.config import config


def fetchDemand(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM demand LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT demand_value, demand_value_id, status
            FROM demand;""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"demand_value": row[0], "demand_value_id": row[1], "status": row[2]}
            valueList.append(value)


        cur.close()
        conn.commit()

        return {'valueList': valueList}


    demand_value_id = requestParameters["demand_value_id"]

    cur.execute("""SELECT demand_value
           FROM demand
           WHERE demand_value_id= %(demand_value_id)s ;""", {"demand_value_id": demand_value_id})
    row = cur.fetchone()
    demand_value = row[0]

    return {'demand_value': demand_value}
