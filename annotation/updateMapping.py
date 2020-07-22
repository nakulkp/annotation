import psycopg2
from config import config
from datetime import date


def updateMapping(requestParameters):
    mapping_id = requestParameters["mapping_id"]
    user_id = requestParameters['user_id']
    article_id = requestParameters['article_id']
    comm_desc_id = requestParameters['comm_desc_id']
    commodity_id = requestParameters['commodity_id']
    factor_id = requestParameters['factor_id']
    subfactor_id = requestParameters['subfactor_id']
    subfactorvalue_id = requestParameters['subfactorvalue_id']
    impact_region_id = requestParameters['impact_region_id']
    price_value_id = requestParameters['price_value_id']
    supply_value_id = requestParameters['supply_value_id']
    demand_value_id = requestParameters['demand_value_id']
    event_region_id = requestParameters['event_region_id']
    last_modified_date = date.today()

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
                SET status = 'enabled', last_modified_by= %(user_id)s, article_id = %(article_id)s, comm_desc_id = %(comm_desc_id)s, commodity_id = %(commodity_id)s, factor_id = %(factor_id)s, subfactor_id = %(subfactor_id)s, subfactorvalue_id = %(subfactorvalue_id)s, impact_region_id = %(impact_region_id)s, price_value_id = %(price_value_id)s, supply_value_id = %(supply_value_id)s, demand_value_id = %(demand_value_id)s, event_region_id = %(event_region_id)s
                WHERE mapping_id = %(mapping_id)s;""",
                {'user_id': user_id, 'article_id': article_id, 'comm_desc_id': comm_desc_id,
                 'commodity_id': commodity_id,
                 'factor_id': factor_id, 'subfactor_id': subfactor_id, 'subfactorvalue_id': subfactorvalue_id,
                 'impact_region_id': impact_region_id, 'price_value_id': price_value_id,
                 'supply_value_id': supply_value_id, 'demand_value_id': demand_value_id,
                 'event_region_id': event_region_id, 'mapping_id': mapping_id}
                )

    cur.execute("""UPDATE master_table
    SET last_modified_by= %(user_id)s, last_modified_date = %(last_modified_date)s
    WHERE article_id=%(article_id)s;""", {'article_id': article_id, 'last_modified_date': last_modified_date})
    cur.close()
    conn.commit()
    conn.close()
    return {'message': "Success"}
