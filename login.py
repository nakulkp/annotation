import psycopg2
from config import config
from passVerify import passVerify


def login(requestParameters):
    conn = None
    try:
        email = requestParameters["email"]
        password = requestParameters["password"]

        email = str(email)

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE email = %(email)s LIMIT 1);", {'email': email})
        userExist = cur.fetchone()
        userExist = userExist[0]

        if not userExist:
            cur.close()
            conn.close()
            return ""

        cur.execute("SELECT pass_key, user_id, privileges FROM users WHERE email = %(email)s", {'email': email})
        row = cur.fetchall()

        pass_key = row[0][0]
        user_id = row[0][1]
        privilege = row[0][2]

        cur.close()
        conn.close()
        if passVerify(pass_key, password):
            return user_id, privilege
        else:
            return "invalid"

    except Exception as error:
        return "Error"

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
