import psycopg2
from annotation.config import config


def adminDeleteSupply(requestParameters):
    conn = None
    supply_value_id = requestParameters['supply_value_id']
    status = requestParameters['status']
    supply_value = requestParameters['supply_value']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  supply SET status = %(status)s, supply_value = %(supply_value)s 
                WHERE supply_value_id=%(supply_value_id)s;""",
                {"status": status, "supply_value": supply_value, "supply_value_id": supply_value_id}
                )
    cur.close()
    conn.commit()
    return "success"
    if conn is not None:
        conn.close()