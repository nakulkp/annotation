import psycopg2
from config import config


def fetchSubFactorValue(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    subfactor_id = requestParameters['subfactor_id']

    cur.execute("SELECT EXISTS (SELECT 1 FROM subfactorvalue_table WHERE status = 'enabled' LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT subfactorvalue, subfactorvalue_id, subfactor_id, status
        FROM subfactorvalue_table WHERE status='enabled' AND subfactor_id = %(subfactor_id)s ORDER BY subfactorvalue_id ASC;""",
                {"subfactor_id": subfactor_id})

    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"subfactorvalue": row[0], "subfactorvalue_id": row[1], "subfactor_id": row[2], "status": row[3]}
        valueList.append(value)

    value = {"subfactorvalue": "-------------------", "subfactorvalue_id": -1, "subfactor_id": -1, "status": 'none'}
    valueList.append(value)

    cur.execute("""SELECT subfactorvalue, subfactorvalue_id, subfactor_id, status
        FROM subfactorvalue_table WHERE status='enabled' EXCEPT (SELECT subfactorvalue, subfactorvalue_id, subfactor_id, status
        FROM subfactorvalue_table WHERE status='enabled' AND subfactor_id = %(subfactor_id)s) ORDER BY subfactorvalue_id ASC;""",
                {"subfactor_id": subfactor_id})
    rows = cur.fetchall()

    for row in rows:
        value = {"subfactorvalue": row[0], "subfactorvalue_id": row[1], "subfactor_id": row[2], "status": row[3]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'data': valueList}
