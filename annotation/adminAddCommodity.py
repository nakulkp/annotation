import psycopg2
from annotation.config import config


def adminAddCommodity(requestParameters):
    conn = None
    try:
        commodities = requestParameters['commodities']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO commodity_table (commodities) VALUES (%s);", (commodities))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_table WHERE commodities = %(commodities)s LIMIT 1);",
                    {'commodities': commodities})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT commodity_id FROM commodity_table WHERE commodities = %(commodities);",
                        {'commodities': commodities})
            commodity_id = cur.fetchone()
            commodity_id = commodity_id[0]
            return {'commodity_id': commodity_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
