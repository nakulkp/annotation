import psycopg2
from annotation.config import config


def adminDeleteSupply(requestParameters):
    try:
        supply_value_id = requestParameters['supply_value_id']
        status = requestParameters['status']
        supply_value = requestParameters['supply_value']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  supply SET status = %(status)s AND supply_value = %(supply_value)s 
                    WHERE supply_value_id=%{supply_value_id}s;""",
                    {"status": status, "supply_value": supply_value, "supply_value_id": supply_value_id}
                    )
        cur.close()
        conn.commit()
        conn.close()

        return "success"

    except Exception as error:
        return "error"
