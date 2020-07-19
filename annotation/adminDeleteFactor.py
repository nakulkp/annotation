import psycopg2
from config import config


def adminDeleteFactor(requestParameters):
    factor_id = requestParameters['factor_id']
    status = requestParameters['status']
    factor = requestParameters['factor']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  factor_table SET status = %(status)s , factor = %(factor)s 
                WHERE factor_id=%(factor_id)s;""",
                {"status": status, "factor": factor, "factor_id": factor_id})

    cur.execute("""UPDATE  subfactor_table SET status = %(status)s WHERE factor_id=%(factor_id)s;""",
                {"status": status, "factor_id": factor_id})

    cur.execute("""UPDATE  subfactorvalue_table SET status = %(status)s WHERE factor_id=%(factor_id)s;""",
                {"status": status, "factor_id": factor_id})

    cur.close()
    conn.commit()

    return {"message": "success"}
