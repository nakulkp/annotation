import psycopg2
from annotation.config import config


def adminAddCategory(requestParameters):
    conn = None
    categories = requestParameters['categories']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("INSERT INTO category_table (categories, status) VALUES (%(categories)s,'enabled');", {'categories': categories})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM category_table WHERE categories = %(categories)s LIMIT 1);",
                {'categories': categories})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT category_id FROM category_table WHERE categories = %(categories)s;",
                    {'categories': categories})
        category_id = cur.fetchone()
        category_id = category_id[0]
        return {'category_id': category_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
