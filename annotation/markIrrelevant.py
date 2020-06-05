import psycopg2
from config import config


def markIrrelevant(requestParameters):
    conn = None
    article_id = requestParameters["article_id"]

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE master_table set status = 'irrelevant'
        where article_id = %(article_id)s;""", {"article_id": article_id})
    cur.close()
    conn.commit()
    conn.close()
    return "Success"
    if conn is not None:
        conn.close()