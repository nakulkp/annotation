import psycopg2
from config import config


def adminAddCommodity(requestParameters):
    conn = None
    commodities = requestParameters['commodities']
    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()


    cur.execute(
        "INSERT INTO commodity_table (commodities,status) VALUES (%(commodities)s,'enabled');", {'commodities': commodities})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM commodity_table WHERE commodities = %(commodities)s LIMIT 1);",
                {'commodities': commodities})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT commodity_id FROM commodity_table WHERE commodities = %(commodities)s;",
                    {'commodities': commodities})
        commodity_id = cur.fetchone()
        commodity_id = commodity_id[0]
        return {'commodity_id': commodity_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
