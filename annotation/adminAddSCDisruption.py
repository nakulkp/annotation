import psycopg2
from config import config


def adminAddSCDisruption(requestParameters):
    conn = None
    sc_disruption_value = requestParameters['sc_disruption_value']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO sc_disruption (sc_disruption_value,status) VALUES (%(sc_disruption_value)s,'enabled');", {'sc_disruption_value': sc_disruption_value})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM sc_disruption WHERE sc_disruption_value = %(sc_disruption_value)s LIMIT 1);",
                {'sc_disruption_value': sc_disruption_value})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT sc_disruption_value_id FROM sc_disruption WHERE sc_disruption_value = %(sc_disruption_value)s;",
                    {'sc_disruption_value': sc_disruption_value})
        sc_disruption_value_id = cur.fetchone()
        sc_disruption_value_id = sc_disruption_value_id[0]
        return {'sc_disruption_value_id': sc_disruption_value_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
