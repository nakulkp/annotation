import psycopg2
from annotation.config import config


def adminUserEdit(requestParameters):
    user_id = requestParameters['user_id']
    username = requestParameters['username']
    email = requestParameters['email']
    phone = requestParameters['phone']
    pass_key = requestParameters['pass_key']
    status = requestParameters['status']
    privilege = requestParameters['privilege']

    # params = config()
    # conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute(
        """UPDATE users
         SET username = %(username)s, email = %(email)s, phone = %(phone)s, pass_key = %(pass_key)s, status = %(status)s, privilege = %(privilege)s
         WHERE user_id = %(user_id)s;""",
        {'user_id': user_id, 'username': username, 'email': email, 'phone': phone, 'pass_key': pass_key,
         'status': status, 'privilege': privilege})

    cur.close()
    conn.commit
    conn.close()
    return ({"message": "success"})
