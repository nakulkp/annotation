import psycopg2
from annotation.config import config


def adminAddFactorValue(requestParameters):
    conn = None
    try:
        factor_value = requestParameters['factor_value']

        //params = config()
        //conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO factor_value_table (factor_value) VALUES (%s);", (factor_value))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM factor_value_table WHERE factor_value = %(factor_value)s LIMIT 1);",
                    {'factor_value': factor_value})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT factor_value_id FROM factor_value_table WHERE factor_value = %(factor_value);",
                        {'factor_value': factor_value})
            factor_value_id = cur.fetchone()
            factor_value_id = factor_value_id[0]
            return {'factor_value_id': factor_value_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
