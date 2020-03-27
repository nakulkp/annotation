import psycopg2
from annotation.config import config


def adminAddSubCategory(requestParameters):
    conn = None
    sub_categories = requestParameters['sub_categories']

    #params = config()
    #conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO subcategory_table (sub_categories,status) VALUES (%(sub_categories)s,'enabled');", {'sub_categories': sub_categories})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM subcategory_table WHERE sub_categories = %(sub_categories)s LIMIT 1);",
                {'sub_categories': sub_categories})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.execute("SELECT sub_category_id FROM subcategory_table WHERE sub_categories = %(sub_categories)s;",
                    {'sub_categories': sub_categories})
        sub_category_id = cur.fetchone()
        sub_category_id = sub_category_id[0]
        return {'sub_category_id': sub_category_id}
    else:
        return "failed"
    if conn is not None:
        conn.close()
