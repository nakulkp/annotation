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

    sql = "INSERT INTO users(username,email,phone,pass_key,privilege) VALUES (%(username)s,%(email)s,%(phone)s,%(pass_key)s),%(privilege)s)"

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute(sql,
                {'username': username, 'email': email, 'phone': phone, 'pass_key': pass_key, 'privilege': privilege})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE username = %(username)s LIMIT 1);", {'username': username})
    userExists = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if userExists:
        return "successful"
    else:
        return "failed"
