import psycopg2
from config import config


def adminDeleteRegionOfEvent(requestParameters):
    event_region_id = requestParameters['event_region_id']
    status = requestParameters['status']
    event_region = requestParameters['event_region']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  region_of_event SET status = %(status)s , event_region = %(event_region)s 
                WHERE event_region_id=%(event_region_id)s;""",
                {"status": status, "event_region": event_region, "event_region_id": event_region_id})
    cur.close()
    conn.commit()

    return {"message": "success"}
