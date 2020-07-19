import psycopg2
from config import config

from fetchCommodity import fetchCommodity
from fetchCommodityDescription import fetchCommodityDescription
from fetchDemand import fetchDemand
from fetchFactor import fetchFactor
from fetchRegionOfImpact import fetchRegionOfImpact
from fetchPrice import fetchPrice
from fetchRegionOfEvent import fetchRegionOfEvent
from fetchSubFactor import fetchSubFactor
from fetchSubFactorValue import fetchSubFactorValue
from fetchSupply import fetchSupply


def fetchMapping(requestParameters):
    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    article_id = requestParameters["article_id"]
    cur.execute("""SELECT exists (SELECT 1 FROM mapping_table
                WHERE article_id= %(article_id)s AND status = 'enabled' LIMIT 1);""", {'article_id': article_id})
    articleExist = cur.fetchone()
    articleExist = articleExist[0]

    if not articleExist:
        cur.close()
        conn.close()
        return {'message': "no matching data"}

    cur.execute(
        """SELECT comm_desc_id, commodity_id, factor_id, subfactor_id, subfactorvalue_id, impact_region_id, price_value_id, supply_value_id, demand_value_id, event_region_id, mapping_id, user_id 
        FROM mapping_table 
        WHERE article_id= %(article_id)s AND status = 'enabled';""", {"article_id": article_id}
    )

    rows = cur.fetchall()
    returnList = []

    for row in rows:
        comm_desc_id = row[0]
        commodity_id = row[1]
        factor_id = row[2]
        subfactor_id = row[3]
        subfactorvalue_id = row[4]
        impact_region_id = row[5]
        price_value_id = row[6]
        supply_value_id = row[7]
        demand_value_id = row[8]
        event_region_id = row[9]
        mapping_id = row[10]
        user_id = row[11]

        loopVal = {'mapping_id': mapping_id, 'user_id': user_id, 'comm_desc_id': comm_desc_id,
                   'commodity_id': commodity_id, 'factor_id': factor_id, 'subfactor_id': subfactor_id,
                   'subfactorvalue_id': subfactorvalue_id, 'impact_region_id': impact_region_id,
                   'price_value_id': price_value_id, 'supply_value_id': supply_value_id,
                   'demand_value_id': demand_value_id, 'event_region_id': event_region_id,
                   "factor" : fetchFactor({'is_null' : "no", 'factor_id':factor_id, 'page': 0}),
                    "commodities" : fetchCommodity({'is_null' : "no", 'commodity_id': commodity_id, 'page': 0}),
                    "demand_value" : fetchDemand({'is_null' : "no", 'demand_value_id': demand_value_id, 'page': 0}),
                    "impact_region" : fetchRegionOfImpact({'is_null' : "no", 'impact_region_id': impact_region_id, 'page': 0}),
                    "subfactorvalue" : fetchSubFactorValue({'is_null' : "no", 'subfactorvalue_id': subfactorvalue_id, 'page': 0}),
                    "price_value" : fetchPrice({'is_null' : "no", 'price_value_id': price_value_id, 'page': 0}),
                    "comm_desc" : fetchCommodityDescription({'is_null' : "no", 'comm_desc_id': comm_desc_id, 'page': 0}),
                    "event_region" : fetchRegionOfEvent({'is_null' : "no", 'event_region_id': event_region_id, 'page': 0}),
                    "subfactor" : fetchSubFactor({'is_null' : "no", 'subfactor_id': subfactor_id, 'page': 0}),
                    "supply_value" : fetchSupply({'is_null' : "no", 'supply_value_id': supply_value_id, 'page': 0})
               }
        returnList.append(loopVal)


        cur.close()
        conn.close()

    #success_message = {"message": "success"}
    #returnList.append(success_message)
    finalList = {'data': returnList, "message": "success"}
    return finalList
