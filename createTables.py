import psycopg2
from config import config

def createTables():
    commands = (
        """
        CREATE TABLE users (
            user_id VARCHAR(25),
            name VARCHAR(50) NOT NULL,
            email TEXT NOT NULL,
            phone VARCHAR(20) NOT NULL,
            password TEXT NOT NULL,
            PRIMARY KEY(user_id),
            UNIQUE(user_id,email,phone)
            )  
        """,
        """
        CREATE TABLE regions(
            countries VARCHAR(50) NOT NULL,
            country_id VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE
        )
        """,
        """
        CREATE TABLE commodity(
        
        )
        """,

        """
        CREATE TABLE mapping
        """,
        """
        CREATE TABLE master_article (
            article_id INTEGER,
            headline TEXT,
            content TEXT,
            owner VARCHAR(50),
            release_date DATE DEFAULT CURRENT_DATE,
            source TEXT,
            url TEXT,
            user_id VARCHAR(50) REFERENCES users(user_id) ON DELETE RESTRICT,
            country_id TEXT,
            PRIMARY KEY(article_id),
            UNIQUE(article_id,country_id),
            FOREIGN KEY () REFERENCES  users()
        )
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError)as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    createTables()
