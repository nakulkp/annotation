import psycopg2
from annotation.config import config


def adminDeleteCommodity(requestParameters):
    try:
        commodity_id = requestParameters['commodity_id']
        status = requestParameters['status']
        commodities = requestParameters['commodities']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  commodity_table SET status = %(status)s AND commodities = %(commodities)s 
                    WHERE commodity_id=%{commodity_id}s;""",
                    {"status": status, "commodities": commodities, "commodity_id": commodity_id}
                    )

        return "success"

    except Exception as error:
        return "error"
