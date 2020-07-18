import psycopg2
from config import config


def adminAddFactor(requestParameters):
    conn = None
    factor = requestParameters['factor']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO factor_table (factor,status) VALUES (%(factor)s,'enabled');", {'factor': factor})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM factor_table WHERE factor = %(factor)s LIMIT 1);",
                {'factor': factor})
    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if valueExists:
        cur.execute("SELECT factor_id FROM factor_table WHERE factor = %(factor)s;",
                    {'factor': factor})
        factor_id = cur.fetchone()
        factor_id = factor_id[0]
        return {'factor_id': factor_id}
    else:
        return {"message": "failed"}
