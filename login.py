import psycopg2
from config import config
from passVerify import passVerify


def login(requestParameters):
    username = requestParameters["username"]
    password = requestParameters["password"]

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE username = %(username)s LIMIT 1);", {'username': username})
    userExist = cur.fetchone()
    if not userExist:
        cur.close()
        conn.close()
        return "invalid"

    cur.execute("SELECT pass_key,salt,user_id FROM users WHERE username = %(username)s", {'username': username})
    row = cur.fetchall()

    pass_key = row[0][0]
    salt = row[0][1]
    user_id = row[0][2]

    cur.close()
    conn.close()
    if passVerify(bytes(salt), pass_key, password):
        return user_id + " valid "
    else:
        return "invalid"
