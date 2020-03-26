import psycopg2
from annotation.config import config


def articleContent(requestParameters):
    conn = None
    try:
        user_id = requestParameters['user_id']
        flag = requestParameters['flag']

        if user_id or flag is None:
            return "Parameters not found"

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        userExists = cur.execute("SELECT exists (SELECT 1 FROM table WHERE user_id = %(user_id)s LIMIT 1);",
                                 {'user_id': user_id})
        userExists = userExists[0]
        if not userExists:
            cur.close()
            conn.commit()
            conn.close()
            return "user does not exist"

        cur.execute("SELECT article_id FROM master_table WHERE user_id= %(user_id)s AND status=todo;",
                    {"user_id": user_id})
        articleList = cur.fetchall()
        article_id = articleList[flag]

        cur.execute(
            """SELECT owner, release_date, source, url, headline, content 
            FROM master_table 
            WHERE article_id= %(article_id)s AND status=todo;""",
            {"article_id": article_id}
        )

        owner = cur.fetchone()
        release_date = cur.fetchone()
        source = cur.fetchone()
        url = cur.fetchone()
        headline = cur.fetchone()
        content = cur.fetchone()

        cur.execute("""SELECT countries
            FROM region
            WHERE status = 'enabled';""")
        countries = cur.fetchall()
        countries = countries[0]

        cur.execute("""SELECT commodities
            FROM commodity_table
            WHERE status = 'enabled';""")
        commodities = cur.fetchall()
        commodities = commodities[0]

        cur.execute("""SELECT categories
                FROM category_table
            WHERE status = 'enabled';""")
        categories = cur.fetchall()
        categories = categories[0]

        cur.execute("""SELECT sub_categories
                FROM subcategory_table
            WHERE status = 'enabled';""")
        sub_categories = cur.fetchall()
        sub_categories = sub_categories[0]

        cur.execute("""SELECT moving_factors
                FROM moving_factor_table
            WHERE status = 'enabled';""")
        moving_factors = cur.fetchall()
        moving_factors = moving_factors[0]

        cur.execute("""SELECT factor_value
                FROM factor_value_table
            WHERE status = 'enabled';""")
        factor_value = cur.fetchall()
        factor_value = factor_value[0]

        cur.execute("""SELECT price_value
                FROM price
            WHERE status = 'enabled';""")
        price_value = cur.fetchall()
        price_value = price_value[0]

        cur.execute("""SELECT supply_value
                FROM supply
            WHERE status = 'enabled';""")
        supply_value = cur.fetchall()
        supply_value = supply_value[0]

        cur.execute("""SELECT demand_value
                FROM demand
            WHERE status = 'enabled';""")
        demand_value = cur.fetchall()
        demand_value = demand_value[0]

        cur.execute("""SELECT sc_disruption_value
                FROM sc_disruption
            WHERE status = 'enabled';""")
        sc_disruption_value = cur.fetchall()
        sc_disruption_value = sc_disruption_value[0]

        cur.close()
        conn.commit()
        conn.close()
        returnList = [countries, commodities, categories, sub_categories, moving_factors, factor_value, price_value,
                      supply_value, demand_value, sc_disruption_value, owner, release_date, source, url, headline,
                      content]

        return returnList

    except Exception as error:
        return "Error= "
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

