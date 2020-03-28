import psycopg2
from annotation.config import config


def articleContentId(requestParameters):
    conn = None
    article_id = requestParameters['article_id']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""SELECT COUNT(article_id)
        FROM master_table
        WHERE article_id = %(article_id)s AND status='todo';""", {"article_id": article_id})
    todoCount = cur.fetchone()
    todoCount = todoCount[0]

    if todoCount == 0:
        return {"message": "empty"}

    cur.execute("""SELECT owner, release_date, source, url, headline, content, question 
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

    returnList = {'owner': owner, 'release_date': release_date, 'source': source, 'url': url, 'headline': headline,
                  'content': content, 'question': question, 'article_id': article_id}

    cur.execute("""SELECT exists (SELECT 1 FROM mapping_table
            WHERE article_id= %(article_id)s LIMIT 1);""", {'article_id': article_id})

    articleExist = cur.fetchone()
    articleExist = articleExist[0]
    if articleExist:
        cur.execute(
            """SELECT country_id, commodity_id, category_id, subcategory_id, moving_factor_id, factor_value_id, price_value_id, supply_value_id, demand_value_id, sc_disruption_value_id 
            FROM mapping_table 
            WHERE article_id= %(article_id)s;""", {"article_id": article_id}
        )

        row = cur.fetchall()
        country_id = row[0][0]
        commodity_id = row[0][1]
        category_id = row[0][2]
        subcategory_id = row[0][3]
        moving_factor_id = row[0][4]
        factor_value_id = row[0][5]
        price_value_id = row[0][6]
        supply_value_id = row[0][7]
        demand_value_id = row[0][8]
        sc_disruption_value_id = row[0][9]
        user_id = row[0][10]

        extraVal = {'user_id': user_id, 'country_id': country_id,
                    'commodity_id': commodity_id, 'category_id': category_id, 'subcategory_id': subcategory_id,
                    'moving_factor_id': moving_factor_id, 'factor_value_id': factor_value_id,
                    'price_value_id': price_value_id, 'supply_value_id': supply_value_id,
                    'demand_value_id': demand_value_id, 'sc_disruption_value_id': sc_disruption_value_id}

        returnList.update(extraVal)

    cur.close()
    conn.commit()
    return returnList
