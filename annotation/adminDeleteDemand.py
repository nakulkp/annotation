import psycopg2
from annotation.config import config


def adminDeleteDemand(requestParameters):
    try:
        demand_value_id = requestParameters['demand_value_id']
        status = requestParameters['status']
        demand_value = requestParameters['demand_value']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  demand SET status = %(status)s AND demand_value = %(demand_value)s 
                    WHERE demand_value_id=%{demand_value_id}s;""",
                    {"status": status, "demand_value": demand_value, "demand_value_id": demand_value_id}
                    )
        cur.close()
        conn.commit()
        conn.close()

        return "success"

    except Exception as error:
        return "error"
