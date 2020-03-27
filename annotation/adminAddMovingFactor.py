import psycopg2
from annotation.config import config


def adminAddMovingFactor(requestParameters):
    conn = None
    try:
        moving_factors = requestParameters['moving_factors']

        //params = config()
        //conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO moving_factor_table (moving_factors) VALUES (%s);", (moving_factors))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table WHERE moving_factors = %(moving_factors)s LIMIT 1);",
                    {'moving_factors': moving_factors})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT moving_factor_id FROM moving_factor_table WHERE moving_factors = %(moving_factors);",
                        {'moving_factors': moving_factors})
            moving_factor_id = cur.fetchone()
            moving_factor_id = moving_factor_id[0]
            return {'moving_factor_id': moving_factor_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
