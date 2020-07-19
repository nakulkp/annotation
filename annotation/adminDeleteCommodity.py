import psycopg2
from config import config


def adminDeleteCommodity(requestParameters):
    commodity_id = requestParameters['commodity_id']
    status = requestParameters['status']
    commodities = requestParameters['commodities']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  commodity_table SET status = %(status)s , commodities = %(commodities)s 
                WHERE commodity_id=%(commodity_id)s;""",
                {"status": status, "commodities": commodities, "commodity_id": commodity_id})

    cur.execute("""UPDATE  commodity_description_table SET status = %(status)s WHERE commodity_id=%(commodity_id)s;""",
                {"status": status, "commodity_id": commodity_id})

    cur.close()
    conn.commit()

    return {"message": "success"}
