import psycopg2
from config import config


def adminAddFactorValue(requestParameters):
    conn = None
    factor_value = requestParameters['factor_value']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO factor_value_table (factor_value,status) VALUES (%(factor_value)s,'enabled');", {'factor_value': factor_value})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM factor_value_table WHERE factor_value = %(factor_value)s LIMIT 1);",
                {'factor_value': factor_value})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT factor_value_id FROM factor_value_table WHERE factor_value = %(factor_value)s;",
                    {'factor_value': factor_value})
        factor_value_id = cur.fetchone()
        factor_value_id = factor_value_id[0]
        return {'factor_value_id': factor_value_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
