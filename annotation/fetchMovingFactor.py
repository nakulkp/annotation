import psycopg2
from annotation.config import config


def fetchMovingFactor():
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table  WHERE status = 'enabled' LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT moving_factors, moving_factor_id, status
        FROM moving_factor_table
        WHERE status = 'enabled';""")
    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"moving_factors": row[0], "moving_factor_id": row[1], "status": row[2]}
        valueList.append(value)


    cur.close()
    conn.commit()

    return {'valueList': valueList}
