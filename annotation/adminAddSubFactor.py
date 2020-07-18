import psycopg2
from config import config


def adminAddSubFactor(requestParameters):
    conn = None
    subfactor = requestParameters['subfactor']
    factor_id = requestParameters['factor_id']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO subfactor_table (subfactor,factor_id,status) VALUES (%(subfactor)s,%(factor_id)s,'enabled');",
        {'subfactor': subfactor, 'factor_id': factor_id})
    conn.commit()

    cur.execute(
        "SELECT EXISTS (SELECT 1 FROM subfactor_table WHERE subfactor = %(subfactor)s AND factor_id= %(factor_id)s LIMIT 1);",
        {'subfactor': subfactor, 'factor_id': factor_id})
    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if valueExists:
        cur.execute(
            "SELECT subfactor_id FROM subfactor_table WHERE subfactor = %(subfactor)s AND factor_id= %(factor_id)s;",
            {'subfactor': subfactor, 'factor_id': factor_id})
        subfactor_id = cur.fetchone()
        subfactor_id = subfactor_id[0]
        return {'subfactor_id': subfactor_id}
    else:
        return {"message": "failed"}
