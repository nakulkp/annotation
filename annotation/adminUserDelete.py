import psycopg2
from config import config


def adminUserDelete(requestParameters):
    user_id = requestParameters['user_id']

    # params = config()
    # conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute("""UPDATE master_table 
    SET user_id = 1, status = 'disabled'
    WHERE user_id = %(user_id)s;""", {'user_id': user_id})

    cur.execute("""UPDATE mapping_table 
    SET user_id = 1, status = 'disabled'
    WHERE user_id = %(user_id)s;""", {'user_id': user_id})

    conn.commit()
    cur.close()
    conn.close()
    return {"message": "success"}
