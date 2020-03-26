import psycopg2
from annotation.config import config


def adminDeleteRegion(requestParameters):
    conn = None
    try:
        country_id = requestParameters['country_id']
        status = requestParameters['status']
        countries = requestParameters['countries']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  region SET status = %(status)s AND countries = %(countries)s 
                    WHERE country_id=%{country_id}s;""",
                    {"status": status, "countries": countries, "country_id": country_id}
                    )
        cur.close()
        conn.commit()

        return "success"

    except Exception as error:
        return "error"

    finally:
        if conn is not None:
            conn.close()