import psycopg2
from annotation.config import config


def adminAddPrice(requestParameters):
    conn = None
    try:
        price_value = requestParameters['price_value']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO price (price_value) VALUES (%s);", (price_value))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM price WHERE price_value = %(price_value)s LIMIT 1);",
                    {'price_value': price_value})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT price_value_id FROM price WHERE price_value = %(price_value);",
                        {'price_value': price_value})
            price_value_id = cur.fetchone()
            price_value_id = price_value_id[0]
            return {'price_value_id': price_value_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
