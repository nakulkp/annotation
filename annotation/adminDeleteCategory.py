import psycopg2
from annotation.config import config


def adminDeleteCategory(requestParameters):
    conn = None
    try:
        category_id = requestParameters['category_id']
        status = requestParameters['status']
        categories = requestParameters['categories']

        #params = config()
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        cur.execute("""UPDATE  category_table SET status = %(status)s AND categories = %(categories)s 
                    WHERE category_id=%{category_id}s;""",
                    {"status": status, "categories": categories, "category_id": category_id}
                    )

        cur.close()
        conn.commit()

        return "success"

    except Exception as error:
        return "error"
    finally:
        if conn is not None:
            conn.close()
