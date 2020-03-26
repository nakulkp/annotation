import psycopg2
from config import config


def articleContent(requestParameters):
    conn = None
    try:
        user_id = requestParameters['user_id']
        flag = requestParameters['flag']

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
            return 'user does not exists'

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

        cur.execute("""SELECT countries, country_id
            FROM region
            WHERE status = 'enabled';""")
        countries = cur.fetchall()
        countries = countries[0]
        country_id = countries[1]

        cur.execute("""SELECT commodities, commodity_id
            FROM commodity_table
            WHERE status = 'enabled';""")
        commodities = cur.fetchall()
        commodities = commodities[0]
        commodity_id = countries[1]

        cur.execute("""SELECT categories, category_id
                FROM category_table
            WHERE status = 'enabled';""")
        categories = cur.fetchall()
        categories = categories[0]
        category_id = countries[1]

        cur.execute("""SELECT sub_categories, subcategory_id
                FROM subcategory_table
            WHERE status = 'enabled';""")
        sub_categories = cur.fetchall()
        sub_categories = sub_categories[0]
        subcategory_id = countries[1]

        cur.execute("""SELECT moving_factors, moving_factor_id
                FROM moving_factor_table
            WHERE status = 'enabled';""")
        moving_factors = cur.fetchall()
        moving_factors = moving_factors[0]
        moving_factor_id = countries[1]

        cur.execute("""SELECT factor_value, factor_value_id
                FROM factor_value_table
            WHERE status = 'enabled';""")
        factor_value = cur.fetchall()
        factor_value = factor_value[0]
        factor_value_id = countries[1]

        cur.execute("""SELECT price_value, price_value_id
                FROM price
            WHERE status = 'enabled';""")
        price_value = cur.fetchall()
        price_value = price_value[0]
        price_value_id = countries[1]

        cur.execute("""SELECT supply_value, supply_value_id
                FROM supply
            WHERE status = 'enabled';""")
        supply_value = cur.fetchall()
        supply_value = supply_value[0]
        supply_value_id = countries[1]

        cur.execute("""SELECT demand_value, demand_value_id
                FROM demand
            WHERE status = 'enabled';""")
        demand_value = cur.fetchall()
        demand_value = demand_value[0]
        demand_value_id = countries[1]

        cur.execute("""SELECT sc_disruption_value, sc_disruption_value_id
                FROM sc_disruption
            WHERE status = 'enabled';""")
        sc_disruption_value = cur.fetchall()
        sc_disruption_value = sc_disruption_value[0]
        sc_disruption_value_id = countries[1]

        cur.close()
        conn.commit()
        conn.close()
        returnList = [countries, commodities, categories, sub_categories, moving_factors, factor_value, price_value,
                      supply_value, demand_value, sc_disruption_value, owner, release_date, source, url, headline,
                      content, country_id, commodity_id, category_id, subcategory_id, moving_factor_id, factor_value_id,
                      price_value_id, supply_value_id, demand_value_id, sc_disruption_value_id]

        return returnList

    except Exception as error:
        return "Error"
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
