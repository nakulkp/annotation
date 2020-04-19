import psycopg2
from annotation.config import config


def updateMapping(requestParameters):
    mapping_id = requestParameters["mapping_id"]
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

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM mapping_table WHERE mapping_id = %(mapping_id)s LIMIT 1);",
                {'mapping_id': mapping_id})
    mappingExists = cur.fetchone()
    mappingExists = mappingExists[0]

    if not mappingExists:
        cur.close()
        conn.close()
        return {'message': "no matching mapping"}

    cur.execute("""UPDATE mapping_table 
                SET status = 'enabled', last_modified_by= %(user_id)s, article_id = %(article_id)s, country_id = %(country_id)s, commodity_id = %(commodity_id)s, category_id = %(category_id)s, subcategory_id = %(subcategory_id)s, moving_factor_id = %(moving_factor_id)s, factor_value_id = %(factor_value_id)s, price_value_id = %(price_value_id)s, supply_value_id = %(supply_value_id)s, demand_value_id = %(demand_value_id)s, sc_disruption_value_id = %(sc_disruption_value_id)s, last_modified = current_timestamp AT TIME ZONE 'UTC'
                WHERE mapping_id = %(mapping_id)s;""",
                {'user_id': user_id, 'article_id': article_id, 'country_id': country_id, 'commodity_id': commodity_id,
                 'category_id': category_id, 'subcategory_id': subcategory_id, 'moving_factor_id': moving_factor_id,
                 'factor_value_id': factor_value_id, 'price_value_id': price_value_id,
                 'supply_value_id': supply_value_id, 'demand_value_id': demand_value_id,
                 'sc_disruption_value_id': sc_disruption_value_id, 'mapping_id': mapping_id}
                )
    cur.close()
    conn.commit()
    conn.close()
    return {'message': "Success"}

