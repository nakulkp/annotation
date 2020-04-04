import psycopg2
from annotation.config import config


def fetchPrice(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    is_null = requestParameters['is_null']

    if is_null == 'NULL':
        cur.execute("SELECT EXISTS (SELECT 1 FROM price LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT price_value, price_value_id, status
            FROM price;""")
        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"price_value": row[0], "price_value_id": row[1], "status": row[2]}
            valueList.append(value)

        cur.close()
        conn.commit()

        return {'valueList': valueList}

    price_value_id = requestParameters["price_value_id"]

    cur.execute("""SELECT price_value
           FROM price
           WHERE price_value_id= %(price_value_id)s ;""", {"price_value_id": price_value_id})
    row = cur.fetchone()
    price_value = row[0]

    return {'price_value': price_value}
