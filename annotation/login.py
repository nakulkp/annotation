import psycopg2
from annotation.config import config
from annotation.passVerify import passVerify


def login(requestParameters):
    conn = None
    email = requestParameters["email"]
    password = requestParameters["password"]

    email = str(email)

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")

    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE email = %(email)s LIMIT 1);", {'email': email})

    userExist = cur.fetchone()
    userExist = userExist[0]

    if not userExist:
        cur.close()
        conn.close()
        return ""

    cur.execute("""SELECT pass_key, user_id, privilege FROM users WHERE email =%(email)s;""",
                {'email': email})

    row = cur.fetchall()
    pass_key = row[0][0]
    user_id = row[0][1]
    privilege = row[0][2]

    conn.commit()
    cur.close()
    conn.close()
    if passVerify(pass_key, password) == True:
        return user_id, privilege
    else:
        return "invalid"
    if conn is not None:
        conn.close()
