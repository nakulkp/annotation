import psycopg2
from config import config


def adminDeleteSubCategory(requestParameters):
    conn = None
    sub_category_id = requestParameters['sub_category_id']
    status = requestParameters['status']
    sub_categories = requestParameters['sub_categories']
    category = requestParameters['category']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  subcategory_table SET status = %(status)s , sub_categories = %(sub_categories)s , category_id = %(category)s
                WHERE sub_category_id=%(sub_category_id)s;""",
                {"status": status, "sub_categories": sub_categories, "sub_category_id": sub_category_id, 'category': category}
                )
    cur.close()
    conn.commit()

    return "success"
    if conn is not None:
        conn.close()