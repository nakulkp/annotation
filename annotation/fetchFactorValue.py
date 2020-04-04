import psycopg2
from annotation.config import config


def fetchFactorValue(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    is_null = requestParameters['is_null']

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM factor_value_table LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT factor_value, factor_value_id, status
            FROM factor_value_table;""")
        rows = cur.fetchall()
        valueList = []
        for row in rows:
            value = {"factor_value": row[0], "factor_value_id": row[1], "status": row[2]}
            valueList.append(value)


        cur.close()
        conn.commit()

        return {'valueList': valueList}

    factor_value_id = requestParameters["factor_value_id"]

    cur.execute("""SELECT factor_value
           FROM factor_value_table
           WHERE factor_value_id= %(factor_value_id)s ;""", {"factor_value_id": factor_value_id})
    row = cur.fetchone()
    factor_value = row[0]

    return factor_value
