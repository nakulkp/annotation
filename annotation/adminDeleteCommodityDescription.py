import psycopg2
from config import config


def adminDeleteCommodityDescription(requestParameters):
    comm_desc_id = requestParameters['comm_desc_id']
    status = requestParameters['status']
    comm_desc = requestParameters['comm_desc']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  commodity_description_table SET status = %(status)s , comm_desc = %(comm_desc)s 
                WHERE comm_desc_id=%(comm_desc_id)s;""",
                {"status": status, "comm_desc": comm_desc, "comm_desc_id": comm_desc_id})
    cur.close()
    conn.commit()

    return {"message": "success"}
