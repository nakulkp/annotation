import psycopg2
from annotation.config import config


def fetchRegion(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM region LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT countries, country_id, status
            FROM region;""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"countries": row[0], "country_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'valueList': valueList}

    country_id = requestParameters["country_id"]

    cur.execute("""SELECT countries
           FROM region
           WHERE country_id= %(country_id)s ;""", {"country_id": country_id})
    row = cur.fetchone()
    countries = row[0]

    return countries
