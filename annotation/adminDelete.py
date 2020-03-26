import psycopg2
from annotation.config import config


def adminDelete(requestParameters):
    try:
        id_name = requestParameters['id_name']
        table_name = requestParameters['table_name']
        value_name = requestParameters['value_name']

        id = requestParameters[id_name]
        status = requestParameters['status']
        value = requestParameters[value_name]

        query = "UPDATE " + table_name + " SET status = %(status)s AND " + value_name + " = %(value)s WHERE " + id_name + "=%{id}s;"

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(query, {"status": status, "value": value, "id": id})

        return "success"

    except Exception as error:
        return "error"
