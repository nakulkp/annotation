import psycopg2
from config import config
from datetime import date


def markWithQuestion(requestParameters):
    user_id = requestParameters['user_id']
    last_modified_date = date.today()
    last_modified_by = user_id
    article_id = requestParameters["article_id"]
    question = requestParameters["question"]

    # params = config()
    # conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE master_table
     SET question = %(question)s, last_modified_date = %(last_modified_date)s,last_modified_by= %(last_modified_by)s , status = 'marked'
        WHERE article_id = %(article_id)s;""",
                {"question": question, "article_id": article_id, 'last_modified_date': last_modified_date,
                 'last_modified_by': last_modified_by})

    cur.close()
    conn.commit()
    conn.close()
    return {"message": "success"}
