import psycopg2
from annotation.config import config


def articleContent(requestParameters):
    conn = None
    try:
        user_id = requestParameters['user_id']
        flag = requestParameters['flag']

        #params = config()
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()
        userExists = cur.execute("SELECT exists (SELECT 1 FROM table WHERE user_id = %(user_id)s LIMIT 1);",
                                 {'user_id': user_id})
        userExists = userExists[0]
        if not userExists:
            cur.close()
            conn.commit()
            conn.close()
            return 'user does not exists'

        cur.execute("SELECT article_id FROM master_table WHERE user_id= %(user_id)s AND status=todo;",
                    {"user_id": user_id})
        articleList = cur.fetchall()
        article_id = articleList[flag]

        cur.execute(
            """SELECT owner, release_date, source, url, headline, content, question 
            FROM master_table 
            WHERE article_id= %(article_id)s AND status=todo;""",
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

        cur.close()
        conn.commit()
        returnList = {'owner': owner, 'release_date': release_date, 'source': source, 'url': url, 'headline': headline,
                      'content': content, 'question': question, 'article_id': article_id, 'country_id': country_id,
                      'commodity_id': commodity_id, 'category_id': category_id, 'subcategory_id': subcategory_id,
                      'moving_factor_id': moving_factor_id, 'factor_value_id': factor_value_id,
                      'price_value_id': price_value_id, 'supply_value_id': supply_value_id,
                      'demand_value_id': demand_value_id, 'sc_disruption_value_id': sc_disruption_value_id}

        return returnList

    except Exception as error:
        return "Error"
    finally:
        if conn is not None:
            conn.close()
