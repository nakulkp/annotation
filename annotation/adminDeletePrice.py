import psycopg2
from annotation.config import config


def adminDeletePrice(requestParameters):
    try:
        price_value_id = requestParameters['price_value_id']
        status = requestParameters['status']
        price_value = requestParameters['price_value']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  price SET status = %(status)s AND price_value = %(price_value)s 
                    WHERE price_value_id=%{price_value_id}s;""",
                    {"status": status, "price_value": price_value, "price_value_id": price_value_id}
                    )
        cur.close()
        conn.commit()
        conn.close()

        return "success"

    except Exception as error:
        return "error"
