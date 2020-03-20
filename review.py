import psycopg2
from config import config


def review(requestParameters):
    user_id = requestParameters["user_id"]

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute("SELECT privilege FROM users WHERE user_id = %(user_id)s; ",
                {'user_id': user_id})
    privilege = cur.fetchone()
    privilege = privilege[0]

    if privilege == 'admin':
        cur.execute("""SELECT article_id, headline, status, question, url
         FROM master_table;""")
        reviewValues = cur.fetchall()

    else:
        cur.execute("""SELECT article_id, headline, status, question, url
                 FROM master_table
                 WHERE user_id=%(user_id)s;""", {'user_id': user_id})

    cur.close()
    conn.commit()
    conn.close()
    return reviewValues
