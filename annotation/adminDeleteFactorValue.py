import psycopg2
from annotation.config import config


def adminDeleteFactorValue(requestParameters):
    try:
        factor_value_id = requestParameters['factor_value_id']
        status = requestParameters['status']
        factor_value = requestParameters['factor_value']

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("""UPDATE  factor_value_table SET status = %(status)s AND factor_value = %(factor_value)s 
                    WHERE factor_value_id=%{factor_value_id}s;""",
                    {"status": status, "factor_value": factor_value, "factor_value_id": factor_value_id}
                    )

        cur.close()
        conn.commit()
        conn.close()

        return "success"

    except Exception as error:
        return "error"
