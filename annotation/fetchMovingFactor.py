import psycopg2
from annotation.config import config


def fetchMovingFactor():
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT moving_factors, moving_factor_id, status
        FROM moving_factor_table
        WHERE status = 'enabled';""")
    rows = cur.fetchall()
    valueList = []
    i = 0
    for row in rows:
        value = {"moving_factors": row[i][0], "moving_factor_id": row[i][1], "status": row[i][2]}
        valueList.append(value)
        i += 1

    cur.close()
    conn.commit()

    return {'valueList': valueList}
