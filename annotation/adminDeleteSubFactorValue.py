import psycopg2
from config import config


def adminDeleteSubFactorValue(requestParameters):
    subfactorvalue_id = requestParameters['subfactorvalue_id']
    status = requestParameters['status']
    subfactorvalue = requestParameters['subfactorvalue']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  subfactorvalue_table SET status = %(status)s , subfactorvalue = %(subfactorvalue)s 
                WHERE subfactorvalue_id=%(subfactorvalue_id)s;""",
                {"status": status, "subfactorvalue": subfactorvalue, "subfactorvalue_id": subfactorvalue_id})

    cur.close()
    conn.commit()

    return {"message": "success"}
