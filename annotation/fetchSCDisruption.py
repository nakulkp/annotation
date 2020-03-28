import psycopg2
from annotation.config import config


def fetchSCDisruption():
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM sc_disruption WHERE status = 'enabled' LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT sc_disruption_value, sc_disruption_value_id, status
        FROM sc_disruption
        WHERE status = 'enabled';""")
    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"sc_disruption_value": row[0], "sc_disruption_value_id": row[1], "status": row[2]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'valueList': valueList}
