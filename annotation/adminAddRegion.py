import psycopg2
from annotation.config import config


def adminAddRegion(requestParameters):
    conn = None
    countries = requestParameters['countries']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO region (countries,status) VALUES (%(countries)s,'enabled');", {'countries': countries})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM region WHERE countries = %(countries)s LIMIT 1);",
                {'countries': countries})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT country_id FROM region WHERE countries = %(countries)s;",
                    {'countries': countries})
        country_id = cur.fetchone()
        country_id = country_id[0]
        return {'country_id': country_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
