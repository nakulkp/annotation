import psycopg2
from config import config


def adminAddCommodityDescription(requestParameters):
    conn = None
    comm_desc = requestParameters['comm_desc']
    commodity_id = requestParameters['commodity_id']
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO commodity_description_table (comm_desc,commodity_id,status) VALUES (%(comm_desc)s,%(commodity_id)s,'enabled');",
        {'comm_desc': comm_desc, 'commodity_id': commodity_id})
    conn.commit()

    cur.execute(
        "SELECT EXISTS (SELECT 1 FROM commodity_description_table WHERE comm_desc = %(comm_desc)s AND commodity_id = %(commodity_id)s LIMIT 1);",
        {'comm_desc': comm_desc, 'commodity_id': commodity_id})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute(
            "SELECT comm_desc_id FROM commodity_description_table WHERE comm_desc = %(comm_desc)s AND commodity_id = %(commodity_id)s;",
            {'comm_desc': comm_desc, 'commodity_id': commodity_id})
        comm_desc_id = cur.fetchone()
        comm_desc_id = comm_desc_id[0]
        conn.close()
        return {'comm_desc_id': comm_desc_id}
    else:
        conn.close()
        return {"message": "failed"}



