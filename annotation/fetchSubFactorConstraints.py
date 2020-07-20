import psycopg2
from config import config


def fetchSubFactorConstraints(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    factor_id = requestParameters['factor_id']

    cur.execute("SELECT EXISTS (SELECT 1 FROM subfactor_table WHERE status = 'enabled' LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT subfactor, subfactor_id, factor_id, status
        FROM subfactor_table WHERE status='enabled' AND factor_id = %(factor_id)s ORDER BY subfactor_id ASC;""",
                {"factor_id": factor_id})

    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"subfactor": row[0], "subfactor_id": row[1], "factor_id": row[2], "status": row[3]}
        valueList.append(value)

    value = {"subfactor": "-------------------", "subfactor_id": -1, "factor_id": -1, "status": 'none'}
    valueList.append(value)

    cur.execute("""SELECT subfactor, subfactor_id, factor_id, status
        FROM subfactor_table WHERE status='enabled' EXCEPT (SELECT subfactor, subfactor_id, factor_id, status
        FROM subfactor_table WHERE status='enabled' AND factor_id = %(factor_id)s) ORDER BY subfactor_id ASC;""",
                {"factor_id": factor_id})
    rows = cur.fetchall()

    for row in rows:
        value = {"subfactor": row[0], "subfactor_id": row[1], "factor_id": row[2], "status": row[3]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'data': valueList}
