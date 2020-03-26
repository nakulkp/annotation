import psycopg2
from config import config


def articleSave(requestParameters):
    conn = None
    try:
        user_id = requestParameters['user_id']
        article_id = requestParameters['article_id']
        country_id = requestParameters['country_id']
        commodity_id = requestParameters['commodity_id']
        category_id = requestParameters['category_id']
        subcategory_id = requestParameters['subcategory_id']
        moving_factor_id = requestParameters['moving_factor_id']
        factor_value_id = requestParameters['factor_value_id']
        price_value_id = requestParameters['price_value_id']
        supply_value_id = requestParameters['supply_value_id']
        demand_value_id = requestParameters['demand_value_id']
        sc_disruption_value_id = requestParameters['sc_disruption_value_id']
        question = requestParameters['question']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""INSERT INTO master_table (user_id, article_id, country_id, commodity_id, category_id, subcategory_id, moving_factor_id, factor_value_id, price_value_id, supply_value_id, demand_value_id, sc_disruption_value_id)
        VALUES (%(user_id)s, %(article_id)s, %(country_id)s, %(commodity_id)s, %(category_id)s, %(subcategory_id)s, %(moving_factor_id)s, %(factor_value_id)s, %(price_value_id)s, %(supply_value_id)s, %(demand_value_id)s, %(sc_disruption_value_id)s;);""",
                    {'user_id': user_id, 'article_id': article_id, 'country_id': country_id,
                     'commodity_id': commodity_id,
                     'category_id': category_id, 'subcategory_id': subcategory_id, 'moving_factor_id': moving_factor_id,
                     'factor_value_id': factor_value_id, 'price_value_id': price_value_id, 'supply_value_id': supply_value_id,
                     'demand_value_id': demand_value_id, 'sc_disruption_value_id': sc_disruption_value_id})
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
        return 'Error'
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
