import psycopg2
from config import config


def adminAddPrice(requestParameters):
    conn = None
    price_value = requestParameters['price_value']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO price (price_value,status) VALUES (%(price_value)s,'enabled');", {'price_value': price_value})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM price WHERE price_value = %(price_value)s LIMIT 1);",
                {'price_value': price_value})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT price_value_id FROM price WHERE price_value = %(price_value)s;",
                    {'price_value': price_value})
        price_value_id = cur.fetchone()
        price_value_id = price_value_id[0]
        return {'price_value_id': price_value_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
