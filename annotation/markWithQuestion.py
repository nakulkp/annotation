import psycopg2
from annotation.config import config


def markWithQuestion(requestParameters):
    article_id = requestParameters["article_id"]
    question = requestParameters["question"]

    # params = config()
    # conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE master_table SET question = %(question)s, status = 'marked'
        WHERE article_id = %(article_id)s;""", {"question": question, "article_id": article_id})

    cur.close()
    conn.commit()
    conn.close()
    return "Success"
