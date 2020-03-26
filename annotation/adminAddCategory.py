import psycopg2
from annotation.config import config


def adminAddCategory(requestParameters):
    try:
        categories = requestParameters['categories']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (username, email, phone, pass_key, status, privilege) VALUES (%s, %s, %s, %s, %s, %s);",
            (username, email, phone, pass_key, status, privilege))
        conn.commit()
        cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE email = %(email)s LIMIT 1);",
                    {'email': email})
        userExists = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if userExists:
            return {'category_id':category_id}
        else:
            return "failed"


        return {'category_id':category_id}

    except Exception as error:
        return "error"
