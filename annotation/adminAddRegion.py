import psycopg2
from annotation.config import config


def adminAddRegion(requestParameters):
    conn = None
    try:
        countries = requestParameters['countries']

        #params = config()
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO region (countries) VALUES (%s);", (countries))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM region WHERE countries = %(countries)s LIMIT 1);",
                    {'countries': countries})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT country_id FROM region WHERE countries = %(countries);",
                        {'countries': countries})
            country_id = cur.fetchone()
            country_id = country_id[0]
            return {'country_id': country_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
