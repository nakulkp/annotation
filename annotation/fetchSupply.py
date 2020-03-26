import psycopg2
from annotation.config import config


def fetchSupply():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""SELECT supply_value
            FROM supply
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
