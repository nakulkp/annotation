import psycopg2
from annotation.config import config
from annotation.passHash import passHash


def userSignUp(requestParameters):
    conn = None
    try:
        username = requestParameters["username"]
        print("1")
        email = requestParameters["email"]
        print("2")
        phone = requestParameters["phone"]
        print("3")
        password = requestParameters["password"]
        print("4")
        privilege = requestParameters["privilege"]
        print("5")
        pass_key = passHash(password)
        status = 'True'

        params = config()
        conn = psycopg2.connect(**params)
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

    except Exception as error:
        return error

    finally:
        if conn is not None:
            conn.close()
