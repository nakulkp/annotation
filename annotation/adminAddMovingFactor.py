import psycopg2
from config import config


def adminAddMovingFactor(requestParameters):
    conn = None
    moving_factors = requestParameters['moving_factors']
    sub_category_id = requestParameters['sub_category_id']
    commodity_id = requestParameters['commodity_id']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO moving_factor_table (moving_factors,status,sub_category_id,commodity_id) VALUES (%(moving_factors)s,'enabled',%(sub_category_id)s,%(commodity_id)s);",
        {'moving_factors': moving_factors, 'sub_category_id': sub_category_id, 'commodity_id': commodity_id})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table WHERE moving_factors = %(moving_factors)s LIMIT 1);",
                {'moving_factors': moving_factors})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT moving_factor_id FROM moving_factor_table WHERE moving_factors = %(moving_factors)s;",
                    {'moving_factors': moving_factors})
        moving_factor_id = cur.fetchone()
        moving_factor_id = moving_factor_id[0]
        return {'moving_factor_id': moving_factor_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
