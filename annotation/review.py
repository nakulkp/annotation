import psycopg2
from annotation.config import config


def review(requestParameters):
    user_id = requestParameters["user_id"]
    filter_ = requestParameters["filter"]

    #params = config()
    #conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    page = requestParameters['page']
    factor = requestParameters['factor']

    offset = (page-1)*factor
    limit = factor

    cur.execute("SELECT privilege FROM users WHERE user_id = %(user_id)s; ",
                 {'user_id': user_id})
    privilege = cur.fetchone()
    privilege = privilege[0]

    dataCount = 0
    pageCount = 0
    
    if filter_ == 'all':
        if privilege == '1':
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                FROM master_table ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table;""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1    

        else:
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                        FROM master_table
                        WHERE user_id=%(user_id)s ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s;""", {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1     

    elif filter_ == 'todo':
        if privilege == '1':
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                FROM master_table WHERE status='todo' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='todo';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1    

        else:
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                        FROM master_table
                        WHERE user_id=%(user_id)s AND WHERE status='todo' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND WHERE status='todo';""", {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1     

    elif filter_ == 'irrelevant':
        if privilege == '1':
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                FROM master_table WHERE status='irrelevant' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='irrelevant';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1    

        else:
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                        FROM master_table
                        WHERE user_id=%(user_id)s AND WHERE status='irrelevant' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND WHERE status='irrelevant';""", {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1     

    elif filter_ == 'completed':
        if privilege == '1':
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                FROM master_table WHERE status='completed' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='completed';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1    

        else:
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                        FROM master_table
                        WHERE user_id=%(user_id)s AND WHERE status='completed' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND WHERE status='completed';""", {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1     

    elif filter_ == 'marked':
        if privilege == '1':
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                FROM master_table WHERE status='marked' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='marked';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1    

        else:
            cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                        FROM master_table
                        WHERE user_id=%(user_id)s AND WHERE status='marked' ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()
            
            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND WHERE status='marked';""", {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0]//factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1     

    finalValues = []
    for rv in reviewValues:
        owner = rv[0]
        cur.execute(
            """SELECT username FROM users WHERE user_id = %(user_id)s LIMIT 1;""",
            {"user_id": owner}
        )
        row = cur.fetchall()
        ownername = row[0][0]
        lst = list(rv)
        lst[0] = ownername
        finalValues.append(lst)

    cur.close()
    conn.commit()
    conn.close()
    return {'data': finalValues, 'pages': pageCount, 'limit': limit, 'offset': offset},