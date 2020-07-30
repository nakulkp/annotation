import psycopg2
#from config import config
#Run this program to create database

def createTables():
    commands = (
        """
        CREATE TABLE users ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            user_id SERIAL NOT NULL, 
            username varchar NOT NULL,
            email varchar NOT NULL,
            phone varchar NOT NULL,
            pass_key varchar NOT NULL,
            status varchar NOT NULL,
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
            headline varchar NOT NULL,
            content varchar NOT NULL,
            owner varchar NOT NULL,
            release_date date NOT NULL,
            source text,
            url text,
            question text,
            last_modified_date DATE default CURRENT_DATE,
            last_modified_by INTEGER,
            status varchar NOT NULL,
            CONSTRAINT master_table_pkey PRIMARY KEY (article_id)
        );
        """,
        """
        CREATE TABLE mapping_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            mapping_id SERIAL NOT NULL,            
            user_id INTEGER NOT NULL,
            article_id INTEGER NOT NULL,
            commodity_id INTEGER NOT NULL,
            comm_desc_id INTEGER DEFAULT -1,
            factor_id INTEGER NOT NULL,
            subfactor_id INTEGER NOT NULL,
            subfactorvalue_id INTEGER NOT NULL,
            impact_region_id INTEGER NOT NULL,
            event_region_id INTEGER NOT NULL,
            price_value_id INTEGER DEFAULT -1,
            supply_value_id INTEGER DEFAULT -1,
            demand_value_id INTEGER DEFAULT -1,
            status varchar,
            last_modified_by INTEGER,
            deleted_on_date DATE,
            deleted_by INTEGER,
            CONSTRAINT mapping_table_pkey PRIMARY KEY (mapping_id)
        );   
        """,
        """
        CREATE TABLE region_of_event( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            event_region varchar NOT NULL,
            event_region_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT region_of_event_pkey PRIMARY KEY (event_region_id)
        );
        """,
        """
        CREATE TABLE commodity_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            commodities varchar NOT NULL,
            commodity_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT commodityTable_pkey PRIMARY KEY (commodity_id)
        );
        """,
        """
        CREATE TABLE commodity_description_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            comm_desc varchar NOT NULL,
            comm_desc_id SERIAL NOT NULL,
            commodity_id INTEGER NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT commodity_description_table_pkey PRIMARY KEY (comm_desc_id)
        );
        """,
        """
        CREATE TABLE factor_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            factor varchar NOT NULL,
            factor_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT factor_table_pkey PRIMARY KEY (factor_id)
        );
        """,
        """
        CREATE TABLE subfactor_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            subfactor varchar NOT NULL,
            subfactor_id SERIAL NOT NULL,
            factor_id INTEGER NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT subfactor_table_pkey PRIMARY KEY (subfactor_id)
        );
        """,
        """
        CREATE TABLE subfactorvalue_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            subfactorvalue varchar NOT NULL,
            subfactorvalue_id SERIAL NOT NULL,
            factor_id INTEGER NOT NULL,
            subfactor_id INTEGER NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT subfactorvalue_table_pkey PRIMARY KEY (subfactorvalue_id)
        );
        """,
        """
        CREATE TABLE region_of_impact_table ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            impact_region varchar NOT NULL,
            impact_region_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT region_of_impact_table_pkey PRIMARY KEY (impact_region_id)
        );
        """,
        """
        CREATE TABLE price ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            price_value varchar NOT NULL,
            price_value_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT price_pkey PRIMARY KEY (price_value_id)
        );
        """,
        """
        CREATE TABLE supply ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            supply_value varchar NOT NULL,
            supply_value_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT supply_pkey PRIMARY KEY (supply_value_id)
        );
        """,
        """
        CREATE TABLE demand ( 
            created_date timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
            demand_value varchar NOT NULL,
            demand_value_id SERIAL NOT NULL,
            status varchar NOT NULL,
            CONSTRAINT demand_pkey PRIMARY KEY (demand_value_id)
        );
        """
    )
    conn = None
    try:
        #params = config()
        #conn = psycopg2.connect(**params)
        conn = psycopg2.connect(host="localhost", database="annotation", user="postgres", password="pass")
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        cur = conn.cursor()
        cur.execute()

    except(Exception, psycopg2.DatabaseError)as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    createTables()