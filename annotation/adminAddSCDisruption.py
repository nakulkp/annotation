import psycopg2
from annotation.config import config


def adminAddSCDisruption(requestParameters):
    conn = None
    try:
        sc_disruption_value = requestParameters['sc_disruption_value']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO sc_disruption (sc_disruption_value) VALUES (%s);", (sc_disruption_value))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM sc_disruption WHERE sc_disruption_value = %(sc_disruption_value)s LIMIT 1);",
                    {'sc_disruption_value': sc_disruption_value})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT sc_disruption_value_id FROM sc_disruption WHERE sc_disruption_value = %(sc_disruption_value);",
                        {'sc_disruption_value': sc_disruption_value})
            sc_disruption_value_id = cur.fetchone()
            sc_disruption_value_id = sc_disruption_value_id[0]
            return {'sc_disruption_value_id': sc_disruption_value_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
