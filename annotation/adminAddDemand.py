import psycopg2
from annotation.config import config


def adminAddDemand(requestParameters):
    conn = None
    demand_value = requestParameters['demand_value']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO demand (demand_value) VALUES (%(demand_value)s);", {'demand_value': demand_value})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM demand WHERE demand_value = %(demand_value)s LIMIT 1);",
                {'demand_value': demand_value})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT demand_value_id FROM demand WHERE demand_value = %(demand_value)s;",
                    {'demand_value': demand_value})
        demand_value_id = cur.fetchone()
        demand_value_id = demand_value_id[0]
        return {'demand_value_id': demand_value_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
