import psycopg2
from annotation.config import config


def articleContent(requestParameters):
    user_id = requestParameters['user_id']
    flag = requestParameters['flag']

    flag = int(flag)

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    userExists = cur.execute("SELECT exists (SELECT 1 FROM users WHERE user_id = %(user_id)s LIMIT 1);",
                             {'user_id': user_id})
    userExists = cur.fetchone()
    userExists = userExists[0]
    if not userExists:
        cur.close()
        conn.commit()
        conn.close()
        return 'user does not exists'

    cur.execute("""SELECT COUNT(article_id)
        FROM master_table
        WHERE user_id = %(user_id)s AND status='todo';""", {"user_id": user_id})
    todoCount = cur.fetchone()
    todoCount = todoCount[0]

    if todoCount == 0:
        return {"message": "empty"}

    cur.execute("SELECT article_id FROM master_table WHERE user_id= %(user_id)s AND status='todo';",
                {"user_id": user_id})

    articleList = cur.fetchall()
    article_id = articleList[flag]

    cur.execute(
        """SELECT owner, release_date, source, url, headline, content, question 
        FROM master_table 
        WHERE article_id= %(article_id)s AND status='todo';""",
        {"article_id": article_id}
    )

    row = cur.fetchall()
    owner = row[0][0]
    release_date = row[0][1]
    source = row[0][2]
    url = row[0][3]
    headline = row[0][4]
    content = row[0][5]
    question = row[0][6]
    
    cur.execute(
        """SELECT username FROM users WHERE user_id = %(user_id)s LIMIT 1;""",
        {"user_id": owner}
    )
    row = cur.fetchall()
    ownername = row[0][0]

    returnList = {'owner': ownername, 'release_date': release_date, 'source': source, 'url': url, 'headline': headline,
                  'content': content, 'question': question, 'article_id': article_id, 'count': todoCount}

    cur.close()
    conn.commit()
    return returnList
