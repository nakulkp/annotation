# SAFE EXAMPLES. DO THIS!
# SELECT exists (SELECT 1 FROM table WHERE column = <value> LIMIT 1);
# cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});
import psycopg2
from config import config
#Run this program to create database

def createTables():
    commands = (
        """
        INSERT INTO test2 (blah) VALUES ('blah2');
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError)as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    createTables()