import psycopg2
from annotation.config import config


def adminDeleteSubCategory(requestParameters):
    conn = None
    sub_category_id = requestParameters['sub_category_id']
    status = requestParameters['status']
    sub_categories = requestParameters['sub_categories']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  subcategory_table SET status = %(status)s AND sub_categories = %(sub_categories)s 
                WHERE sub_category_id=%(sub_category_id)s;""",
                {"status": status, "sub_categories": sub_categories, "sub_category_id": sub_category_id}
                )
    cur.close()
    conn.commit()

    return "success"
    if conn is not None:
        conn.close()