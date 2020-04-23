import psycopg2
from annotation.config import config


def articleCount(requestParameters):
    conn = None
    user_id = requestParameters['user_id']
    
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    
    cur.execute("SELECT privilege FROM users WHERE user_id = %(user_id)s; ",
                {'user_id': user_id})
    privilege = cur.fetchone()
    privilege = privilege[0]

    if privilege == '1':
        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'todo';""")

        valueList = cur.fetchall()
        todoCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'irrelevant';""")

        valueList = cur.fetchall()
        irrelevantCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'completed';""")

        valueList = cur.fetchall()
        completedCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'marked';""")

        valueList = cur.fetchall()
        markedCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table;""")

        valueList = cur.fetchall()
        allCount = valueList[0]

    else:
        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'todo' AND user_id = %(user_id)s;""",
                {'user_id': user_id})

        valueList = cur.fetchall()
        todoCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'irrelevant' AND user_id = %(user_id)s;""",
                {'user_id': user_id})

        valueList = cur.fetchall()
        irrelevantCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'completed' AND user_id = %(user_id)s;""",
                {'user_id': user_id})

        valueList = cur.fetchall()
        completedCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table
            WHERE status = 'marked' AND user_id = %(user_id)s;""",
                {'user_id': user_id})

        valueList = cur.fetchall()
        markedCount = valueList[0]

        cur.execute("""SELECT COUNT(article_id)
            FROM master_table AND user_id = %(user_id)s;""",
                {'user_id': user_id})

        valueList = cur.fetchall()
        allCount = valueList[0]

    cur.close()
    conn.commit()

    return {'todo':todoCount[0], 'irrelevant': irrelevantCount[0], 'completed': completedCount[0], 'marked':markedCount[0], 'all': allCount[0]}