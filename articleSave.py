import psycopg2
from annotation.config import config


def articleSave(requestParameters):
    conn = None
    try:
        user_id = requestParameters['user_id']
        article_id = requestParameters['article_id']
        countries = requestParameters['countries']
        commodities = requestParameters['commodities']
        categories = requestParameters['categories']
        sub_categories = requestParameters['sub_categories']
        moving_factors = requestParameters['moving_factors']
        factor_value = requestParameters['factor_value']
        price_value = requestParameters['price_value']
        supply_value = requestParameters['supply_value']
        demand_value = requestParameters['demand_value']
        sc_disruption_value = requestParameters['sc_disruption_value']
        question = requestParameters['question']

        paramList = [user_id, article_id, countries, commodities, categories, sub_categories, moving_factors,
                     factor_value, price_value, supply_value, demand_value, sc_disruption_value, question]

        for param in paramList:
            if param is None:
                return "Parameter not found"

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""INSERT INTO master_table (user_id, article_id, countries, commodities, categories, sub_categories, moving_factors, factor_value, price_value, supply_value, demand_value, sc_disruption_value)
        VALUES (%(user_id)s, %(article_id)s, %(countries)s, %(commodities)s, %(categories)s, %(sub_categories)s, %(moving_factors)s, %(factor_value)s, %(price_value)s, %(supply_value)s, %(demand_value)s, %(sc_disruption_value)s;);""",
                    {'user_id': user_id, 'article_id': article_id, 'countries': countries, 'commodities': commodities,
                     'categories': categories, 'sub_categories': sub_categories, 'moving_factors': moving_factors,
                     'factor_value': factor_value, 'price_value': price_value, 'supply_value': supply_value,
                     'demand_value': demand_value, 'sc_disruption_value': sc_disruption_value})
        cur.close()
        conn.commit()

        if question == 'NULL':
            cur = conn.cursor()

            cur.execute("""UPDATE master_table SET status = 'completed'
            WHERE article_id = %(article_id)s;""", {"article_id": article_id})

            cur.close()
            conn.commit()

        conn.close()

        return "success"
    except Exception as error:
        return error
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
