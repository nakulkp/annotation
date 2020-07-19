import psycopg2
from config import config


def adminDeleteRegionOfImpact(requestParameters):
    impact_region_id = requestParameters['impact_region_id']
    status = requestParameters['status']
    impact_region = requestParameters['impact_region']

    # params = config()
    # conn = psycopg2.connect(**params)
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("""UPDATE  region_of_impact_table SET status = %(status)s , impact_region = %(impact_region)s 
                WHERE impact_region_id=%(impact_region_id)s;""",
                {"status": status, "impact_region": impact_region, "impact_region_id": impact_region_id})
    cur.close()
    conn.commit()

    return {"message": "success"}
