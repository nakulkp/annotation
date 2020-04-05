import psycopg2
from annotation.config import config


def articleSave(requestParameters):
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

    owner = requestParameters['owner']
    release_date = requestParameters['release_date']
    source = requestParameters['source']
    url = requestParameters['url']
    headline = requestParameters['headline']
    content = requestParameters['content']
    question = requestParameters['question']
    status = 'marked'

    isAnyMappingIdZero = false

    if user_id == 0 or article_id == 0 or country_id == 0 or commodity_id == 0 or category_id == 0 or subcategory_id == 0 or moving_factor_id == 0 or factor_value_id == 0 or price_value_id == 0 or supply_value_id == 0 or demand_value_id == 0 or sc_disruption_value_id == 0:
        isAnyMappingIdZero = true

    if question == 'NULL':
        status = 'completed'
        question = ''

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE master_table SET owner = %(owner)s , release_date = %(release_date)s , source = %(source)s , headline = %(headline)s, content = %(content)s , question = %(question)s,  status = %(status)s 
    WHERE article_id = %(article_id)s;""",
                {'owner': owner, 'release_date': release_date, 'source': source, 'url': url, 'headline': headline,
                 'content': content, 'question': question, 'status': status, 'article_id': article_id}
                )
    cur.close()
    conn.commit()

    cur = conn.cursor()
    cur.execute("""SELECT EXISTS (SELECT 1 FROM mapping_table
     WHERE article_id = %(article_id)s AND country_id = %(country_id)s AND commodity_id = %(commodity_id)s AND category_id = %(category_id)s AND subcategory_id = %(subcategory_id)s AND moving_factor_id = %(moving_factor_id)s AND factor_value_id = %(factor_value_id)s AND price_value_id = %(price_value_id)s AND supply_value_id = %(supply_value_id)s AND demand_value_id = %(demand_value_id)s AND sc_disruption_value_id = %(sc_disruption_value_id)s LIMIT 1);""",
                {'article_id': article_id, 'country_id': country_id, 'commodity_id': commodity_id,
                 'category_id': category_id, 'subcategory_id': subcategory_id, 'moving_factor_id': moving_factor_id,
                 'factor_value_id': factor_value_id, 'price_value_id': price_value_id,
                 'supply_value_id': supply_value_id, 'demand_value_id': demand_value_id,
                 'sc_disruption_value_id': sc_disruption_value_id})

    mappingExist = cur.fetchone()
    mappingExist = mappingExist[0]

    if not mappingExist and isAnyMappingIdZero:
        cur.execute("""INSERT INTO mapping_table (user_id, article_id, country_id, commodity_id, category_id, subcategory_id, moving_factor_id, factor_value_id, price_value_id, supply_value_id, demand_value_id, sc_disruption_value_id)
        VALUES (%(user_id)s, %(article_id)s, %(country_id)s, %(commodity_id)s, %(category_id)s, %(subcategory_id)s, %(moving_factor_id)s, %(factor_value_id)s, %(price_value_id)s, %(supply_value_id)s, %(demand_value_id)s, %(sc_disruption_value_id)s);""",
                    {'user_id': user_id, 'article_id': article_id, 'country_id': country_id,
                     'commodity_id': commodity_id,
                     'category_id': category_id, 'subcategory_id': subcategory_id, 'moving_factor_id': moving_factor_id,
                     'factor_value_id': factor_value_id, 'price_value_id': price_value_id,
                     'supply_value_id': supply_value_id,
                     'demand_value_id': demand_value_id, 'sc_disruption_value_id': sc_disruption_value_id})
    cur.close()
    conn.commit()
    conn.close()
    if isAnyMappingIdZero return "success article only"
    return "success"
