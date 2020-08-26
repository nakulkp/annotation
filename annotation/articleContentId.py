import psycopg2
from config import config


def articleContentId(requestParameters):
    conn = None
    article_id = requestParameters['article_id']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT COUNT(article_id)
        FROM master_table
        WHERE article_id = %(article_id)s;""", {"article_id": article_id})
    todoCount = cur.fetchone()
    todoCount = todoCount[0]

    if todoCount == 0:
        return {"message": "empty"}

    cur.execute("""SELECT owner, release_date, source, url, headline, content, question, last_modified_date, last_modified_by, status
        FROM master_table 
        WHERE article_id= %(article_id)s;""",
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
    last_modified_date = row[0][7]
    last_modified_by = row[0][8]
    status = row[0][9]

    #cur.execute(
    #    """SELECT username FROM users WHERE user_id = %(user_id)s LIMIT 1;""",
    #    {"user_id": owner}
    #)
    #row = cur.fetchall()
    #ownername = row[0][0]

    returnList = {'owner': owner, 'release_date': release_date, 'source': source, 'url': url, 'headline': headline,
                  'content': content, 'question': question, 'last_modified_date': last_modified_date,
                  'last_modified_by': last_modified_by,'status':status, 'article_id': article_id, 'count': todoCount}
                  
    cur.execute("""UPDATE users SET last_open_article_id = %(article_id)s where user_id = %(user_id)s""", {"article_id": article_id, "user_id": user_id})

    cur.close()
    conn.commit()
    return returnList
