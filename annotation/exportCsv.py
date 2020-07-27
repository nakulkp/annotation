from io import BytesIO as StringIO
import csv
from datetime import datetime
import psycopg2
from config import config


def exportCsv(requestParameters):
    start = requestParameters["start"]
    end = requestParameters["end"]

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    # cur.execute("""select a.article_id, a.headline, a.status, a.question, c.username as owner, a.release_date, a.content, a.source,
    # a.url, b.last_modified, c1.username as last_modified_by, b.status as is_deleted, b.deleted_on_date, c2.username as disabled_by,
    # r.countries, cmd.commodities, cat.categories, scat.sub_categories, mft.moving_factors, fvt.factor_value, p.price_value, sup.supply_value, dem.demand_value, scd.sc_disruption_value
    # from master_table a left join mapping_table b on a.article_id = b.article_id left join users c on a.owner = c.user_id left join users c1 on b.last_modified_by = c1.user_id
    # left join users c2 on b.deleted_by = c2.user_id left join region_of_event r on b.impact_region_id = r.event_region_id
    # left join commodity_table cmd on b.commodity_id = cmd.commodity_id left join category_table cat on b.category_id = cat.category_id
    # left join subcategory_table scat on b.subcategory_id = scat.sub_category_id left join moving_factor_table mft on b.moving_factor_id = mft.moving_factor_id
    # left join factor_value_table fvt on b.factor_value_id = fvt.factor_value_id left join price p on b.price_value_id = p.price_value_id
    # left join supply sup on b.supply_value_id = sup.supply_value_id left join demand dem on b.demand_value_id = dem.demand_value_id
    # left join sc_disruption scd on b.sc_disruption_value_id = scd.sc_disruption_value_id
    # WHERE a.release_date >= %(start)s AND a.release_date <= %(end)s;""", {'start': start, 'end': end})

    cur.execute("""
    SELECT mast.article_id, mast.headline, mast.status, mast.question, usr.username, mast.release_date, mast.content, mast.source, mast.url, mast.last_modified_date, usr2.username, maptbl.status, maptbl.deleted_on_date, maptbl.deleted_by, com.commodities, comds.comm_desc, regevnt.event_region, fctr.factor, sbfctr.subfactor, sbfctrval.subfactorvalue, regimp.impact_region, price.price_value, supply.supply_value, demand.demand_value
    FROM master_table mast 
    LEFT JOIN users usr 
        ON mast.user_id=usr.user_id  
    LEFT JOIN  mapping_table maptbl 
        ON maptbl.article_id=mast.article_id
    LEFT JOIN users usr2 
        ON maptbl.user_id=usr2.user_id  
    LEFT JOIN commodity_table com 
        ON maptbl.commodity_id=com.commodity_id 
    LEFT JOIN commodity_description_table comds 
        ON comds.comm_desc_id=maptbl.comm_desc_id 
    LEFT JOIN  region_of_event regevnt 
        ON regevnt.event_region_id=maptbl.event_region_id 
    LEFT JOIN factor_table fctr 
        ON fctr.factor_id=maptbl.factor_id 
    LEFT JOIN subfactor_table sbfctr 
        ON sbfctr.subfactor_id=maptbl.subfactor_id 
    LEFT JOIN subfactorvalue_table sbfctrval  
        ON sbfctrval.subfactorvalue_id=maptbl.subfactorvalue_id 
    LEFT JOIN region_of_impact_table regimp 
        ON regimp.impact_region_id=maptbl.impact_region_id 
    LEFT JOIN price
        ON price.price_value_id=maptbl.price_value_id
    LEFT JOIN supply 
        ON supply.supply_value_id=maptbl.supply_value_id
    LEFT JOIN demand
        ON demand.demand_value_id=maptbl.demand_value_id
    WHERE mast.release_date >= %(start)s AND mast.release_date <= %(end)s;""",
                {'start': start, 'end': end})
    exportValues = cur.fetchall()

    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(["Article Id", "Title", "Status", "Question", "Owner", "Release Date", "Content", "Source", "URL",
                     "Last Modified", "Last Modified By", "Is Deleted", "Deleted On Date", "Deleted By", "Commodity",
                     "Commodity Description", "Region of Event", "Factor", "Sub Factor", "Sub Factor Value",
                     "Region of Impact", "Price", "Supply", "Demand"])
    for row in exportValues:
        writer.writerow(row)

    return {'data': si.getvalue()}
