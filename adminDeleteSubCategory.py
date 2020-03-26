import psycopg2
from config import config


def adminDeleteSubCategory(requestParameters):
    try:
        sub_category_id = requestParameters['sub_category_id']
        status = requestParameters['status']
        sub_categories = requestParameters['sub_categories']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  subcategory_table SET status = %(status)s AND sub_categories = %(sub_categories)s 
                    WHERE sub_category_id=%{sub_category_id}s;""",
                    {"status": status, "sub_categories": sub_categories, "sub_category_id": sub_category_id}
                    )

        return "success"

    except Exception as error:
        return "error"
