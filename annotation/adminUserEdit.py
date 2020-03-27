import psycopg2
from annotation.config import config

def adminUseredit(requestParameters):
    user_id =requestParameters['user_id']
    username =requestParameters['username']
    email =requestParameters['email']
    phone =requestParameters['phone']
    pass_key =requestParameters['pass_key']
    status =requestParameters['status']
    privilege =requestParameters['privilege']

    #params = config()
    #conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""""")