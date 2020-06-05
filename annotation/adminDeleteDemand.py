import psycopg2
from config import config


def adminDeleteDemand(requestParameters):
    demand_value_id = requestParameters['demand_value_id']
    status = requestParameters['status']
    demand_value = requestParameters['demand_value']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  demand SET status = %(status)s , demand_value = %(demand_value)s 
                WHERE demand_value_id=%(demand_value_id)s;""",
                {"status": status, "demand_value": demand_value, "demand_value_id": demand_value_id}
                )
    cur.close()
    conn.commit()

    return "success"
    if conn is not None:
        conn.close()