import psycopg2
from config import config


def fetchUsers(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    #page = requestParameters['page']
    #offset = (page-1)*10
    #limit = 10

    #cur.execute("""SELECT COUNT(category_id) FROM category_table;""")
    #dataCount = cur.fetchall()
    #dataCount = dataCount[0]
    #pageCount = dataCount[0]//10
    #if (dataCount[0] % 10) != 0 and dataCount[0] > 10:
        #pageCount = pageCount + 1
        
    cur.execute("""SELECT username, user_id FROM users;""")
    rows = cur.fetchall()
    valueList = []

    for row in rows:
        value = {"username": row[0], "user_id": row[1]}
        valueList.append(value)

    cur.close()
    conn.commit()

    return {'data': valueList}
