import psycopg2
from config import config


def adminAddRegionofEvent(requestParameters):
    conn = None
    event_region = requestParameters['event_region']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO region_of_event (event_region,status) VALUES (%(event_region)s,'enabled');", {'event_region': event_region})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM region_of_event WHERE event_region = %(event_region)s LIMIT 1);",
                {'event_region': event_region})
    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if valueExists:
        cur.execute("SELECT event_region_id FROM region_of_event WHERE event_region = %(event_region)s;",
                    {'event_region': event_region})
        event_region_id = cur.fetchone()
        event_region_id = event_region_id[0]
        return {'event_region_id': event_region_id}
    else:
        return "failed"