import psycopg2
from config import config


def adminAddSubFactorValue(requestParameters):
    conn = None
    subfactorvalue = requestParameters['subfactorvalue']
    factor_id = requestParameters['factor_id']
    subfactor_id = requestParameters['subfactor_id']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO subfactorvalue_table (subfactorvalue,factor_id,subfactor_id,status) VALUES (%(subfactorvalue)s,%(factor_id)s,%(subfactor_id)s,'enabled');",
        {'subfactorvalue': subfactorvalue, 'factor_id': factor_id, 'subfactor_id': subfactor_id})
    conn.commit()

    cur.execute(
        "SELECT EXISTS (SELECT 1 FROM subfactorvalue_table WHERE subfactorvalue = %(subfactorvalue)s AND subfactor_id= %(subfactor_id)s LIMIT 1);",
        {'subfactorvalue': subfactorvalue, 'subfactor_id': subfactor_id})
    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if valueExists:
        cur.execute(
            "SELECT subfactorvalue_id FROM subfactorvalue_table WHERE subfactorvalue = %(subfactorvalue)s AND subfactor_id= %(subfactor_id)s;",
            {'subfactorvalue': subfactorvalue, 'subfactor_id': subfactor_id})
        subfactorvalue_id = cur.fetchone()
        subfactorvalue_id = subfactorvalue_id[0]
        return {'subfactorvalue_id': subfactorvalue_id}
    else:
        return {"message": "failed"}
