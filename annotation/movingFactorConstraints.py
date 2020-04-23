import psycopg2
from annotation.config import config


def movingFactorConstraints(requestParameters):
    conn = None
    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()
    cmd_id = requestParameters['commodity_id']
    scat_id = requestParameters['sub_category_id']

    fetchCase = -1;
    if cmd_id != NULL:
        if scat_id != NULL:
            fetchCase = 2
        else:
            fetchCase = 1
    elif scat_id != NULL:
        fetchCase = 0

    if fetchCase == 0:
        cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table WHERE status = 'enabled' LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' AND sub_category_id = %(scat_id)s ORDER BY moving_factor_id ASC;""", {'scat_id': scat_id})

        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"moving_factors": row[0], "moving_factor_id": row[1], "status": row[2], "sub_category_id": row[3], "commodity_id": row[4]}
            valueList.append(value)

            value = {"moving_factors": "-------------------", "moving_factor_id": -1, "status": 'none', "sub_category_id": -1, "commodity_id": -1}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' EXCEPT (SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' AND sub_category_id = %(scat_id)s) ORDER BY moving_factor_id ASC;""", {'scat_id': scat_id})
            
        rows = cur.fetchall()

        cur.close()
        conn.commit()

        return {'data': valueList}

    elif fetchCase == 1:
        cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table WHERE status = 'enabled' LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' AND commodity_id = %(cmd_id)s ORDER BY moving_factor_id ASC;""", {'cmd_id': cmd_id})

        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"moving_factors": row[0], "moving_factor_id": row[1], "status": row[2], "sub_category_id": row[3], "commodity_id": row[4]}
            valueList.append(value)

            value = {"moving_factors": "-------------------", "moving_factor_id": -1, "status": 'none', "sub_category_id": -1, "commodity_id": -1}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' EXCEPT (SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' AND commodity_id = %(cmd_id)s) ORDER BY moving_factor_id ASC;""", {'cmd_id': cmd_id})
            
        rows = cur.fetchall()

        cur.close()
        conn.commit()

        return {'data': valueList}
        
    elif fetchCase == 2:
        cur.execute("SELECT EXISTS (SELECT 1 FROM moving_factor_table WHERE status = 'enabled' LIMIT 1);")

        valueExists = cur.fetchone()
        valueExists = valueExists[0]

        if not valueExists:
            return {'message': "no values"}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' AND commodity_id = %(cmd_id)s OR sub_category_id = %(scat_id)s ORDER BY moving_factor_id ASC;""", {'cmd_id': cmd_id, 'scat_id': scat_id})

        rows = cur.fetchall()
        valueList = []

        for row in rows:
            value = {"moving_factors": row[0], "moving_factor_id": row[1], "status": row[2], "sub_category_id": row[3], "commodity_id": row[4]}
            valueList.append(value)

            value = {"moving_factors": "-------------------", "moving_factor_id": -1, "status": 'none', "sub_category_id": -1, "commodity_id": -1}

        cur.execute("""SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' EXCEPT (SELECT moving_factors, moving_factor_id, status, sub_category_id, commodity_id
            FROM moving_factor_table WHERE status='enabled' AND commodity_id = %(cmd_id)s OR sub_category_id = %(scat_id)s) ORDER BY moving_factor_id ASC;""", {'cmd_id': cmd_id, 'scat_id': scat_id})
            
        rows = cur.fetchall()

        cur.close()
        conn.commit()

        return {'data': valueList}
