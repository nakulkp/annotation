import psycopg2
from annotation.config import config


def adminDeleteSCDisruption(requestParameters):
    conn = None
    try:
        sc_disruption_value_id = requestParameters['sc_disruption_value_id']
        status = requestParameters['status']
        sc_disruption_value = requestParameters['sc_disruption_value']

        //params = config()
        //conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute("""UPDATE  sc_disruption SET status = %(status)s AND sc_disruption_value = %(sc_disruption_value)s 
                    WHERE sc_disruption_value_id=%{sc_disruption_value_id}s;""",
                    {"status": status, "sc_disruption_value": sc_disruption_value,
                     "sc_disruption_value_id": sc_disruption_value_id}
                    )
        cur.close()
        conn.commit()


        return "success"

    except Exception as error:
        return "error"

    finally:
        if conn is not None:
            conn.close()