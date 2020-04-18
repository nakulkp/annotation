import psycopg2
from annotation.config import config


def deleteMapping(requestParameters):
    mapping_id = requestParameters["mapping_id"]
    user_id = requestParameters['user_id']

    conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
    cur = conn.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM mapping_table WHERE mapping_id = %(mapping_id)s LIMIT 1);",
                {'mapping_id': mapping_id})
    mappingExists = cur.fetchone()
    mappingExists = mappingExists[0]

    if not mappingExists:
        cur.close()
        conn.close()
        return {'message': "no matching mapping"}

    cur.execute("""UPDATE mapping_table 
                SET status = 'disabled', deleted_by= %(user_id)s, deleted_on_date = timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
                WHERE mapping_id = %(mapping_id)s;""",
                {'user_id': user_id, 'mapping_id': mapping_id}
                )
    cur.close()
    conn.commit()
    conn.close()
    return {'message': "Success"}

