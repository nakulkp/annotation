import psycopg2
from annotation.config import config


def adminUsersFetch():
    # params = config()
    # conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT user_id, username, email, phone, pass_key, status, privilege
     FROM users;""")
    valueList = []
    rows = cur.fetchall()
    for row in rows:
        value = {"user_id": row[0], "username": row[1], "email": row[2], 'phone': row[3], 'pass_key': row[4],
                 'status': row[5], 'privilege': row[6]}
        valueList.append(value)
    cur.close()
    conn.commit
    conn.close()
    return valueList
