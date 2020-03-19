import psycopg2
from config import config


def articleContent(requestParameters):
    user_id = requestParameters['user_id']
    flag = requestParameters['flag']

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    userExists = cur.execute("SELECT exists (SELECT 1 FROM table WHERE user_id = %(user_id)s LIMIT 1);",
                             {'user_id': user_id})
    if not userExists:
        cur.close()
        conn.commit()
        conn.close()
        return "user does not exist"

    cur.execute("SELECT article_id FROM master_table WHERE user_id= %(user_id)s AND status=todo;", {"user_id": user_id})
    articleList = cur.fetchall()
    article_id = articleList[flag]

    cur.execute("SELECT url FROM master_table WHERE article_id= %(article_id)s AND status=todo;", {"article_id": article_id})
    url = cur.fetchone()

    cur.execute("""SELECT country_id,
        commodity_id, category_id, sub_category_id,
        moving_factor_id, factor_value_id,price_value_id,
        supply_value_id, demand_value_id, sc_disruption_value_id
        FROM mapping_table
        WHERE article_id = %(article_id)s ;""", {"article_id": article_id}
                )

    mappingTable = cur.fetchall()

    country_id = mappingTable[0][0]
    commodity_id = mappingTable[0][1]
    category_id = mappingTable[0][2]
    sub_category_id = mappingTable[0][3]
    moving_factor_id = mappingTable[0][4]
    factor_value_id = mappingTable[0][5]
    price_value_id = mappingTable[0][6]
    supply_value_id = mappingTable[0][7]
    demand_value_id = mappingTable[0][8]
    sc_disruption_value_id = mappingTable[0][9]

    cur.execute("""SELECT countries
        FROM region
        WHERE country_id = %(country_id)s ;""", {"country_id": country_id}
                )
    countries = cur.fetchone()

    cur.execute("""SELECT commodities
        FROM commodity_table
        WHERE commodity_id = %(commodity_id)s ;""", {"commodity_id": commodity_id}
                )
    commodities = cur.fetchone()

    cur.execute("""SELECT categories
            FROM category_table
            WHERE category_id = %(category_id)s ;""", {"category_id": category_id}
                )
    categories = cur.fetchone()

    cur.execute("""SELECT sub_categories
            FROM subcategory_table
            WHERE sub_category_id = %(sub_category_id)s ;""", {"sub_category_id": sub_category_id}
                )
    sub_categories = cur.fetchone()

    cur.execute("""SELECT moving_factors
            FROM moving_factor_table
            WHERE moving_factor_id = %(moving_factor_id)s ;""", {"moving_factor_id": moving_factor_id}
                )
    moving_factors = cur.fetchone()

    cur.execute("""SELECT factor_value
            FROM factor_value_table
            WHERE factor_value_id = %(factor_value_id)s ;""", {"blah": factor_value_id}
                )
    factor_value = cur.fetchone()

    cur.execute("""SELECT price_value
            FROM price
            WHERE price_value_id = %(price_value_id)s ;""", {"price_value_id": price_value_id}
                )
    price_value = cur.fetchone()

    cur.execute("""SELECT supply_value
            FROM supply
            WHERE supply_value_id = %(supply_value_id)s ;""", {"supply_value_id": supply_value_id}
                )
    supply_value = cur.fetchone()

    cur.execute("""SELECT demand_value
            FROM demand
            WHERE demand_value_id = %(demand_value_id)s ;""", {"demand_value_id": demand_value_id}
                )
    demand_value = cur.fetchone()

    cur.execute("""SELECT sc_disruption_value
            FROM sc_disruption
            WHERE sc_disruption_value_id = %(sc_disruption_value_id)s ;""",
                {"sc_disruption_value_id": sc_disruption_value_id}
                )
    sc_disruption_value = cur.fetchone()

    cur.close()
    conn.commit()
    conn.close()
    returnList = [countries, commodities, categories, sub_categories, moving_factors, factor_value, price_value,
                  supply_value, demand_value, sc_disruption_value,url]
    return returnList
