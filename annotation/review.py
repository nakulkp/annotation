import psycopg2
from annotation.config import config


def review(requestParameters):
    user_id = requestParameters["user_id"]

    #params = config()
    #conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    page = requestParameters['page']
    factor = requestParameters['factor']

    offset = (page-1)*factor
    limit = offset + factor

    cur.execute("""SELECT COUNT(article_id) FROM master_table;""")
    dataCount = cur.fetchall()
    dataCount = dataCount[0]
    pageCount = dataCount[0]//factor
    if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
        pageCount = pageCount + 1        

    cur.execute("SELECT privilege FROM users WHERE user_id = %(user_id)s; ",
                {'user_id': user_id})
    privilege = cur.fetchone()
    privilege = privilege[0]

    if privilege == '1':
        cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
            FROM master_table ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {"limit": limit, "offset": offset})
        reviewValues = cur.fetchall()

    else:
        cur.execute("""SELECT owner, article_id, headline, status, question, url, release_date
                    FROM master_table
                    WHERE user_id=%(user_id)s ORDER BY created_date DESC LIMIT %(limit)s OFFSET %(offset)s;""", {'user_id': user_id, "limit": limit, "offset": offset})
        reviewValues = cur.fetchall()

    for rv in reviewValues:
        owner = reviewValues[0][0]
        cur.execute(
            """SELECT username FROM users WHERE user_id = %(user_id)s LIMIT 1;""",
            {"user_id": owner}
        )
        row = cur.fetchall()
        ownername = row[0][0]
        rv.append(row)

    cur.close()
    conn.commit()
    conn.close()
    return {'data': reviewValues, 'pages': pageCount}