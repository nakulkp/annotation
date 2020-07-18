import psycopg2
from config import config


def adminAddRegionofEvent(requestParameters):

    impact_region = requestParameters['impact_region']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO region_of_impact_table (impact_region,status) VALUES (%(impact_region)s,'enabled');",
        {'impact_region': impact_region})
    conn.commit()

    cur.execute("SELECT EXISTS (SELECT 1 FROM region_of_impact_table WHERE impact_region = %(impact_region)s LIMIT 1);",
                {'impact_region': impact_region})
    valueExists = cur.fetchone()
    valueExists = valueExists[0]

    if valueExists:
        cur.execute("SELECT impact_region_id FROM region_of_impact_table WHERE impact_region = %(impact_region)s;",
                    {'impact_region': impact_region})
        impact_region_id = cur.fetchone()
        impact_region_id = impact_region_id[0]
        return {'impact_region_id': impact_region_id}
    else:
        return {"message": "failed"}
