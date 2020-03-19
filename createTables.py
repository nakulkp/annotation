import psycopg2
from config import config
#Run this program to create database

def createTables():
    commands = (
        """
        CREATE TABLE users (
            user_id SERIAL NOT NULL, 
            username character varying(50) COLLATE pg_catalog."default" NOT NULL,
            email text NOT NULL,
            phone character varying(50) NOT NULL,
            pass_key text NOT NULL,
            status boolean NOT NULL,
            privilege character varying(50) NOT NULL,
            CONSTRAINT users_pkey PRIMARY KEY (user_id),
            CONSTRAINT "user" UNIQUE (email, phone)
        );  
        """,
        """
        CREATE TABLE master_table (
            user_id INTEGER NOT NULL,
            article_id SERIAL NOT NULL,
            headline text NOT NULL,
            content text NOT NULL,
            owner character varying(50) NOT NULL,
            release_date date NOT NULL,
            source text,
            url text,
            question text,
            status character varying(50) NOT NULL DEFAULT 'todo'::character varying,
            CONSTRAINT master_table_pkey PRIMARY KEY (article_id)
        );
        """,
        """
        CREATE TABLE mapping_table (
            user_id INTEGER NOT NULL,
            article_id INTEGER NOT NULL,
            country_id INTEGER NOT NULL,
            commodity_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            subcategory_id INTEGER NOT NULL,
            moving_factor_id INTEGER NOT NULL,
            factor_value_id INTEGER NOT NULL,
            price_value_id INTEGER NOT NULL,
            supply_value_id INTEGER NOT NULL,
            demand_value_id INTEGER NOT NULL,
            sc_disruption_value_id INTEGER NOT NULL
        );   
        """,
        """
        CREATE TABLE region(
            countries character varying(50) NOT NULL,
            country_id SERIAL NOT NULL,
            CONSTRAINT region_pkey PRIMARY KEY (country_id)
        );
        """,
        """
        CREATE TABLE commodity_table (
            commodities text NOT NULL,
            commodity_id SERIAL NOT NULL,
            CONSTRAINT "commodityTable_pkey" PRIMARY KEY (commodity_id)
        );
        """,
        """
        CREATE TABLE category_table (
            categories character varying(50) NOT NULL,
            category_id SERIAL NOT NULL,
            CONSTRAINT category_table_pkey PRIMARY KEY (category_id)
        );
        """,
        """
        CREATE TABLE subcategory_table (
            sub_categories character varying(50) NOT NULL,
            sub_category_id SERIAL NOT NULL,
            CONSTRAINT subcategory_table_pkey PRIMARY KEY (sub_category_id)
        );
        """,
        """
        CREATE TABLE moving_factor_table (
            moving_factors character varying(50) NOT NULL,
            moving_factor_id SERIAL NOT NULL,
            CONSTRAINT moving_factor_table_pkey PRIMARY KEY (moving_factor_id)
        );
        """,
        """
        CREATE TABLE factor_value_table (
            factor_value character varying(50) NOT NULL,
            factor_value_id SERIAL NOT NULL,
            CONSTRAINT factor_value_table_pkey PRIMARY KEY (factor_value_id)
        );
        """,
        """
        CREATE TABLE price (
            price_value character varying(50) NOT NULL,
            price_value_id SERIAL NOT NULL,
            CONSTRAINT price_pkey PRIMARY KEY (price_value_id)
        );
        """,
        """
        CREATE TABLE supply (
            supply_value character varying(50) NOT NULL,
            supply_value_id SERIAL NOT NULL,
            CONSTRAINT supply_pkey PRIMARY KEY (supply_value_id)
        );
        """,
        """
        CREATE TABLE demand (
            demand_value character varying(50) NOT NULL,
            demand_value_id SERIAL NOT NULL,
            CONSTRAINT demand_pkey PRIMARY KEY (demand_value_id)
        );
        """,
        """
        CREATE TABLE sc_disruption (
            sc_disruption_value character varying(50) NOT NULL,
            sc_disruption_value_id SERIAL NOT NULL,
            CONSTRAINT sc_disruption_pkey PRIMARY KEY (sc_disruption_value_id)
        );
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
