import psycopg2
from annotation.config import config


def fetchMapping(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    article_id = requestParameters["article_id"]
    cur.execute("""SELECT exists (SELECT 1 FROM mapping_table
                WHERE article_id= %(article_id)s LIMIT 1);""", {'article_id': article_id})
    articleExist = cur.fetchone()
    articleExist = articleExist[0]

    if not articleExist:
        cur.close()
        conn.close()
        return {'message': "no matching data"}

    cur.execute(
        """SELECT country_id, commodity_id, category_id, subcategory_id, moving_factor_id, factor_value_id, price_value_id, supply_value_id, demand_value_id, sc_disruption_value_id, mapping_id, user_id 
        FROM mapping_table 
        WHERE article_id= %(article_id)s;""", {"article_id": article_id}
    )

    rows = cur.fetchall()
    returnList = []

    for row in rows:
        country_id = row[0]
        commodity_id = row[1]
        category_id = row[2]
        subcategory_id = row[3]
        moving_factor_id = row[4]
        factor_value_id = row[5]
        price_value_id = row[6]
        supply_value_id = row[7]
        demand_value_id = row[8]
        sc_disruption_value_id = row[9]
        mapping_id = row[10]
        user_id = row[11]

        loopVal = {'mapping_id': mapping_id, 'user_id': user_id, 'country_id': country_id,
                   'commodity_id': commodity_id, 'category_id': category_id, 'subcategory_id': subcategory_id,
                   'moving_factor_id': moving_factor_id, 'factor_value_id': factor_value_id,
                   'price_value_id': price_value_id, 'supply_value_id': supply_value_id,
                   'demand_value_id': demand_value_id, 'sc_disruption_value_id': sc_disruption_value_id
                   }
        returnList.append(loopVal)

    cur.close()
    conn.close()
    return returnList
