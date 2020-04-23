import psycopg2
from annotation.config import config


def subCategoryConstraints(requestParameters):
    conn = None
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cat_id = requestParameters['category_id']

    cur.execute("SELECT EXISTS (SELECT 1 FROM subcategory_table WHERE status = 'enabled' LIMIT 1);")

    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if not valueExists:
        return {'message': "no values"}

    cur.execute("""SELECT sub_categories, sub_category_id, category_id, status
        FROM subcategory_table WHERE status='enabled' AND category_id = %(cat_id)s ORDER BY sub_category_id ASC;""",  {"cat_id": cat_id})

    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"sub_categories": row[0], "sub_category_id": row[1], "category_id": row[2], "status": row[3]}
        valueList.append(value)
        
    value = {"sub_categories": "-------------------", "sub_category_id": -1, "category_id": -1, "status": 'none'}
    valueList.append(value)
        
    cur.execute("""SELECT sub_categories, sub_category_id, category_id, status
        FROM subcategory_table WHERE status='enabled' EXCEPT (SELECT sub_category_id
        FROM subcategory_table WHERE status='enabled' AND category_id = %(cat_id)s) ORDER BY sub_category_id ASC;""",  {"cat_id": cat_id})
    rows = cur.fetchall()

    for row in rows:
        value = {"sub_categories": row[0], "sub_category_id": row[1], "category_id": row[2], "status": row[3]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'data': valueList}
