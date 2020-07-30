import psycopg2
from config import config
from passHash import passHash


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

    if pass_key == 'NULL':
        cur.execute(
            """UPDATE users
            SET username = %(username)s, email = %(email)s, phone = %(phone)s, status = %(status)s, privilege = %(privilege)s
            WHERE user_id = %(user_id)s;""",
            {'user_id': user_id, 'username': username, 'email': email, 'phone': phone,
             'status': status, 'privilege': privilege})

        cur.execute("""
        UPDATE master_table
        SET owner=%(username)s
        WHERE user_id=%(user_id)s;""",
                    {'username': username, 'user_id': user_id})
        conn.commit()
        cur.close()
        conn.close()
        return ({"message": "success"})

    pass_key = passHash(password)
    cur.execute(
        """UPDATE users
         SET username = %(username)s, email = %(email)s, phone = %(phone)s, pass_key = %(pass_key)s, status = %(status)s, privilege = %(privilege)s
         WHERE user_id = %(user_id)s;""",
        {'user_id': user_id, 'username': username, 'email': email, 'phone': phone, 'pass_key': pass_key,
         'status': status, 'privilege': privilege})

    cur.execute("""
    UPDATE master_table
    SET owner=%(username)s
    WHERE user_id=%(user_id)s;""",
                {'username': username, 'user_id': user_id})

    conn.commit()
    cur.close()
    conn.close()
    return ({"message": "success"})
