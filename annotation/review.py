import psycopg2
from config import config
from psycopg2 import sql


def review(requestParameters):
    user_id = requestParameters["user_id"]
    filter_ = requestParameters["filter"]
    sort_by = requestParameters["sort_by"]
    order_by = requestParameters["order_by"]
    filter_type = requestParameters["filter_type_val"]
    filter_type_val = requestParameters["filter_type_val"]
    page = requestParameters['page']
    factor = requestParameters['factor']

    # params = config()
    # conn = psycopg2.connect(**params)

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()


    offset = (page - 1) * factor
    limit = factor

    cur.execute("SELECT privilege FROM users WHERE user_id = %(user_id)s; ",
                {'user_id': user_id})
    privilege = cur.fetchone()
    privilege = privilege[0]

    dataCount = 0
    pageCount = 0

    if sort_by == '':
        sort_by = 'created_date';

    if order_by == '':
        order_by = 'asc';

    if filter_ == 'all':
        if privilege == '1':
            if order_by == 'asc':
                if filter_type == 'null':
                    query = sql.SQL("""SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                    FROM master_table 
                    ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(field=sql.Identifier(sort_by))
                    cur.execute(query, {"limit": limit, "offset": offset})
                else:
                    query = sql.SQL("""SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                    FROM master_table WHERE {filterType} = %(filterTypeVal)s
                    ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format( filterType=sql.Identifier(filter_type),field=sql.Identifier(sort_by))
                    cur.execute(query, {"filterTypeVal":filter_type_val,"limit": limit, "offset": offset})
            else:
                if filter_type == 'null':
                    query = sql.SQL("""SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                    FROM master_table 
                    ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(field=sql.Identifier(sort_by))
                    cur.execute(query, {"limit": limit, "offset": offset})
                else:
                    query = sql.SQL("""SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                    FROM master_table WHERE {filterType} = %(filterTypeVal)s
                    ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format( filterType=sql.Identifier(filter_type),field=sql.Identifier(sort_by))
                    cur.execute(query, {"filterTypeVal":filter_type_val,"limit": limit, "offset": offset})
                    
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table;""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

        else:
            if order_by == 'asc':
                query = sql.SQL("""SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                 FROM master_table 
                 WHERE user_id=%(user_id)s 
                 ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            else:
                query = sql.SQL("""SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date 
                FROM master_table
                 WHERE user_id=%(user_id)s 
                 ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s;""",
                        {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

    elif filter_ == 'todo':
        if privilege == '1':
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE status='todo' 
                      ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date 
                    FROM master_table
                     WHERE status='todo' 
                     ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='todo';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

        else:
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='todo'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset, "sort_by": sort_by})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='todo'
                       ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset, "sort_by": sort_by})
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND status='todo';""",
                        {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

    elif filter_ == 'irrelevant':
        if privilege == '1':
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE status='irrelevant'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE status='irrelevant'
                       ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='irrelevant';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

        else:
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='irrelevant'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date FROM master_table
                     WHERE user_id=%(user_id)s AND status='irrelevant'
                      ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute(
                """SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND status='irrelevant';""",
                {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

    elif filter_ == 'completed':
        if privilege == '1':
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE status ='completed'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset, "sort_by": sort_by})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE status ='completed'
                       ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset, "sort_by": sort_by})
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='completed';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

        else:
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='completed'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='completed'
                       ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute(
                """SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND status='completed';""",
                {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

    elif filter_ == 'marked':
        if privilege == '1':
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE status='marked'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table WHERE status='marked'
                      ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {"limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute("""SELECT COUNT(article_id) FROM master_table WHERE status='marked';""")
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
            if (dataCount[0] % factor) != 0 and dataCount[0] > factor:
                pageCount = pageCount + 1

        else:
            if order_by == 'asc':
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='marked'
                       ORDER BY {field} ASC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            else:
                query = sql.SQL(
                    """SELECT owner, article_id, headline, status, question, url, release_date, last_modified_date
                     FROM master_table
                      WHERE user_id=%(user_id)s AND status='marked'
                       ORDER BY {field} DESC LIMIT %(limit)s OFFSET %(offset)s;""").format(
                    field=sql.Identifier(sort_by))
                cur.execute(query, {'user_id': user_id, "limit": limit, "offset": offset})
            reviewValues = cur.fetchall()

            cur.execute(
                """SELECT COUNT(article_id) FROM master_table WHERE user_id = %(user_id)s AND status='marked';""",
                {'user_id': user_id})
            dataCount = cur.fetchall()
            dataCount = dataCount[0]
            pageCount = dataCount[0] // factor
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
        ownername = row[0]
        lst = list(rv)
        lst[0] = ownername
        finalValues.append(lst)

    cur.close()
    conn.commit()
    conn.close()
    return {'data': finalValues, 'pages': pageCount, 'limit': limit, 'offset': offset},
