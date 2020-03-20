import psycopg2
from config import config


def markWithQuestion(requestParameters):
    article_id = requestParameters["article_id"]
    question = requestParameters["question"]

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute("""UPDATE master_table set question = %(question)s) AND status = 'marked'
        where article_id = %(article_id)s;""", {"question": question, "article_id": article_id})

    cur.close()
    conn.commit()
    conn.close()
    return
