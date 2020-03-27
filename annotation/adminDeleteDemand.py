import psycopg2
from annotation.config import config


def adminDeleteDemand(requestParameters):
    conn = None
    try:
        demand_value_id = requestParameters['demand_value_id']
        status = requestParameters['status']
        demand_value = requestParameters['demand_value']

        #params = config()
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute("""UPDATE  demand SET status = %(status)s AND demand_value = %(demand_value)s 
                    WHERE demand_value_id=%{demand_value_id}s;""",
                    {"status": status, "demand_value": demand_value, "demand_value_id": demand_value_id}
                    )
        cur.close()
        conn.commit()

        return "success"

    except Exception as error:
        return "error"

    finally:
        if conn is not None:
            conn.close()