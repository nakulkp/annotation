import psycopg2
from annotation.config import config


def adminAddCategory(requestParameters):
    conn = None
    try:
        categories = requestParameters['categories']

        //params = config()
        //conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO category_table (categories) VALUES (%s);", (categories))
        conn.commit()

        cur.execute("SELECT EXISTS (SELECT 1 FROM category_table WHERE categories = %(categories)s LIMIT 1);",
                    {'categories': categories})
        userExists = cur.fetchone()
        userExists = userExists[0]

        if userExists:
            cur.execute("SELECT category_id FROM category_table WHERE categories = %(categories);",
                        {'categories': categories})
            category_id = cur.fetchone()
            category_id = category_id[0]
            return {'category_id': category_id}
        else:
            return "failed"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
