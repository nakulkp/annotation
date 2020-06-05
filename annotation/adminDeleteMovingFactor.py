import psycopg2
from config import config


def adminDeleteMovingFactor(requestParameters):
    conn = None
    moving_factor_id = requestParameters['moving_factor_id']
    status = requestParameters['status']
    moving_factors = requestParameters['moving_factors']
    sub_category_id = requestParameters['sub_category_id']
    commodity_id = requestParameters['commodity_id']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  moving_factor_table SET status = %(status)s , moving_factors = %(moving_factors)s , sub_category_id = %(sub_category_id)s, commodity_id = %(commodity_id)s
                WHERE moving_factor_id=%(moving_factor_id)s;""",
                {"status": status, "moving_factors": moving_factors, "moving_factor_id": moving_factor_id, 'sub_category_id': sub_category_id, 'commodity_id': commodity_id}
                )
    cur.close()
    conn.commit()

    return "success"
    if conn is not None:
        conn.close()