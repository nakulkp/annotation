import psycopg2
from config import config
from passHash import passHash


def userSignUp(requestParameters):
    username = requestParameters["username"]
    email = requestParameters["email"]
    phone = requestParameters["phone"]
    password = requestParameters["password"]
    privilege = requestParameters["privilege"]
    pass_key = passHash(password)
    status = 'enabled'

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT EXISTS (SELECT 1 FROM users
    WHERE email = %(email)s LIMIT 1);""", {'email': email})
    userExists = cur.fetchone()
    userExists = userExists[0]

    if userExists:
        cur.close()
        conn.close()
        return "email already exists"

    cur.execute(
        "INSERT INTO users (username, email, phone, pass_key, status, privilege) VALUES (%s, %s, %s, %s, %s, %s);",
        (username, email, phone, pass_key, status, privilege))
    conn.commit()
    cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE email = %(email)s LIMIT 1);",
                {'email': email})
    userExists = cur.fetchone()
    userExists = userExists[0]

    conn.commit()
    cur.close()
    conn.close()

    if userExists:
        return "successful"
    else:
        return "failed"

