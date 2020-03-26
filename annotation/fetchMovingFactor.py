import psycopg2
from annotation.config import config


def fetchMovingFactor():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""SELECT moving_factors
            FROM moving_factor_table
            WHERE status = 'enabled';""")
        valueList = cur.fetchall()

        cur.close()
        conn.commit()

        return {'valueList': valueList}

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
