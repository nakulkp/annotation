from io import BytesIO as StringIO;
import csv
from datetime import datetime
import psycopg2
from config import config


def exportCsv(requestParameters):

    start = requestParameters["start"]
    end = requestParameters["end"]

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""select a.article_id, a.headline, a.status, a.question, c.username as owner, a.release_date, a.content, a.source, a.url, b.last_modified, c1.username as last_modified_by, b.status as is_deleted, b.deleted_on_date, c2.username as disabled_by, r.countries, cmd.commodities, cat.categories, scat.sub_categories, mft.moving_factors, fvt.factor_value, p.price_value, sup.supply_value, dem.demand_value, scd.sc_disruption_value
     from master_table a left join mapping_table b on a.article_id = b.article_id left join users c on a.owner = c.user_id left join users c1 on b.last_modified_by = c1.user_id left join users c2 on b.deleted_by = c2.user_id left join region r on b.country_id = r.country_id left join commodity_table cmd on b.commodity_id = cmd.commodity_id left join category_table cat on b.category_id = cat.category_id left join subcategory_table scat on b.subcategory_id = scat.sub_category_id left join moving_factor_table mft on b.moving_factor_id = mft.moving_factor_id left join factor_value_table fvt on b.factor_value_id = fvt.factor_value_id left join price p on b.price_value_id = p.price_value_id left join supply sup on b.supply_value_id = sup.supply_value_id left join demand dem on b.demand_value_id = dem.demand_value_id left join sc_disruption scd on b.sc_disruption_value_id = scd.sc_disruption_value_id
     WHERE a.release_date >= %(start)s AND a.release_date <= %(end)s;""", {'start': start, 'end': end})
    exportValues = cur.fetchall()

    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(["Article Id", "Title", "Status", "Question", "Owner", "Release Date", "Content", "Source", "URL", "Last Modified", "Last Modified By", "Is Deleted", "Deleted On Date", "Deleted By", "Region", "Commodity", "Category", "Sub Category", "Moving Factors", "Factor Value", "Price", "Supply", "Demand", "SC Disruption"])
    for row in exportValues:
        writer.writerow(row)

    return {'data': si.getvalue()}