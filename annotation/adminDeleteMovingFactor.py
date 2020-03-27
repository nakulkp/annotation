import psycopg2
from annotation.config import config


def adminDeleteMovingFactor(requestParameters):
    conn = None
    try:
        moving_factor_id = requestParameters['moving_factor_id']
        status = requestParameters['status']
        moving_factors = requestParameters['moving_factors']

        //params = config()
        //conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute("""UPDATE  moving_factor_table SET status = %(status)s AND moving_factors = %(moving_factors)s 
                    WHERE moving_factor_id=%{moving_factor_id}s;""",
                    {"status": status, "moving_factors": moving_factors, "moving_factor_id": moving_factor_id}
                    )
        cur.close()
        conn.commit()

        return "success"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()