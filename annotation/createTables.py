import psycopg2
from config import config
#Run this program to create database

def createTables():
    commands = (
        """
        CREATE TABLE users ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            user_id SERIAL NOT NULL, 
            username character varying() COLLATE pg_catalog."default" NOT NULL,
            email character varying() NOT NULL,
            phone character varying() NOT NULL,
            pass_key character varying() NOT NULL,
            status character varying() NOT NULL,
            privilege character varying(50) NOT NULL,
            CONSTRAINT users_pkey PRIMARY KEY (user_id),
            CONSTRAINT "user" UNIQUE (email, phone)
        );  
        """,
        """
        CREATE TABLE master_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            user_id INTEGER NOT NULL, 
            article_id SERIAL NOT NULL,
            headline character varying() NOT NULL,
            content character varying() NOT NULL,
            owner character varying() NOT NULL,
            release_date date NOT NULL,
            source text,
            url text,
            question text,
            status character varying() NOT NULL,
            CONSTRAINT master_table_pkey PRIMARY KEY (article_id)
        );
        """,
        """
        CREATE TABLE mapping_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
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
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            countries character varying() NOT NULL,
            country_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT region_pkey PRIMARY KEY (country_id)
        );
        """,
        """
        CREATE TABLE commodity_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            commodities character varying() NOT NULL,
            commodity_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT "commodityTable_pkey" PRIMARY KEY (commodity_id)
        );
        """,
        """
        CREATE TABLE category_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            categories character varying() NOT NULL,
            category_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT category_table_pkey PRIMARY KEY (category_id)
        );
        """,
        """
        CREATE TABLE subcategory_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            sub_categories character varying() NOT NULL,
            sub_category_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT subcategory_table_pkey PRIMARY KEY (sub_category_id)
        );
        """,
        """
        CREATE TABLE moving_factor_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            moving_factors character varying() NOT NULL,
            moving_factor_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT moving_factor_table_pkey PRIMARY KEY (moving_factor_id)
        );
        """,
        """
        CREATE TABLE factor_value_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            factor_value character varying() NOT NULL,
            factor_value_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT factor_value_table_pkey PRIMARY KEY (factor_value_id)
        );
        """,
        """
        CREATE TABLE price ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            price_value character varying() NOT NULL,
            price_value_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT price_pkey PRIMARY KEY (price_value_id)
        );
        """,
        """
        CREATE TABLE supply ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            supply_value character varying() NOT NULL,
            supply_value_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT supply_pkey PRIMARY KEY (supply_value_id)
        );
        """,
        """
        CREATE TABLE demand ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            demand_value character varying() NOT NULL,
            demand_value_id SERIAL NOT NULL,
            status character varying() NOT NULL,
            CONSTRAINT demand_pkey PRIMARY KEY (demand_value_id)
        );
        """,
        """
        CREATE TABLE sc_disruption ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            sc_disruption_value character varying() NOT NULL,
            sc_disruption_value_id SERIAL NOT NULL,
            status character varying() NOT NULL,
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