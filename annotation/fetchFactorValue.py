import psycopg2
from annotation.config import config


def fetchFactorValue():
    conn = None
    try:
        #params = config()
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute("""SELECT factor_value
            FROM factor_value_table
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
