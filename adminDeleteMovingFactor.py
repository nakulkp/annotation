import psycopg2
from config import config


def adminDeleteMovingFactor(requestParameters):
    try:
        moving_factor_id = requestParameters['moving_factor_id']
        status = requestParameters['status']
        moving_factors = requestParameters['moving_factors']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  moving_factor_table SET status = %(status)s AND moving_factors = %(moving_factors)s 
                    WHERE moving_factor_id=%{moving_factor_id}s;""",
                    {"status": status, "moving_factors": moving_factors, "moving_factor_id": moving_factor_id}
                    )

        return "success"

    except Exception as error:
        return "error"
