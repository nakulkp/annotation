# SAFE EXAMPLES. DO THIS!
# SELECT exists (SELECT 1 FROM table WHERE column = <value> LIMIT 1);
# cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});

import psycopg2
from config import config
from passVerify import passVerify

def login(userId,password):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT 1 FROM users WHERE username = %(username)s LIMIT 1);",{'username': userId})
    userExist = cur.fetchone()
    if not userExist:
        return 500
    cur.execute("SELECT pass_key,salt, FROM users WHERE username = %(username)s",{'username': userId})
    key,salt = cur.fetchone()
    cur.close()
    conn.close()
    if passVerify(salt,key,password):
        return 200
    else:
        return 500
