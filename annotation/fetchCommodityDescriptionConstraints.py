import psycopg2
from config import config


def fetchCommodityDescriptionConstraints(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    commodity_id = requestParameters['commodity_id']

    cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_description_table WHERE status = 'enabled' LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT comm_desc, comm_desc_id, commodity_id, status
        FROM commodity_description_table WHERE status='enabled' AND commodity_id = %(commodity_id)s ORDER BY comm_desc_id ASC;""",
                {"commodity_id": commodity_id})

    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"comm_desc": row[0], "comm_desc_id": row[1], "commodity_id": row[2], "status": row[3]}
        valueList.append(value)

    value = {"comm_desc": "-------------------", "comm_desc_id": -1, "commodity_id": -1, "status": 'none'}
    valueList.append(value)

    cur.execute("""SELECT comm_desc, comm_desc_id, commodity_id, status
        FROM commodity_description_table WHERE status='enabled' EXCEPT (SELECT comm_desc, comm_desc_id, commodity_id, status
        FROM commodity_description_table WHERE status='enabled' AND commodity_id = %(commodity_id)s) ORDER BY comm_desc_id ASC;""",
                {"commodity_id": commodity_id})
    rows = cur.fetchall()

    for row in rows:
        value = {"comm_desc": row[0], "comm_desc_id": row[1], "commodity_id": row[2], "status": row[3]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'data': valueList}
