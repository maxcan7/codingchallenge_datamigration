#!/usr/bin/env py

import sys
import psycopg2
from configparser import ConfigParser


# Load config file for database
def config(filename=sys.argv[1], section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))

    return db


# Create orders table in postgres database
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE orders (
            source_identifier TEXT,
            subtotal_price INTEGER,
            buyer_accepts_marketing TEXT,
            reference TEXT,
            cart_token TEXT,
            updated_at TIMESTAMP,
            taxes_included TEXT,
            currency TEXT,
            total_weight INTEGER,
            source_name TEXT,
            processed_at TIMESTAMP,
            closed_at TEXT,
            location_id INTEGER,
            gateway TEXT,
            confirmed TEXT,
            user_id INTEGER,
            tags TEXT,
            total_price_usd INTEGER,
            financial_status TEXT,
            id INTEGER PRIMARY KEY,
            note TEXT,
            landing_site TEXT,
            customer_locale TEXT,
            processing_method TEXT,
            total_line_items_price INTEGER,
            cancelled_at TEXT,
            test TEXT,
            app_id INTEGER,
            email TEXT,
            total_tax INTEGER,
            cancel_reason TEXT,
            total_discount TEXT,
            landing_site_ref TEXT,
            number INTEGER,
            phone TEXT,
            total_discounts INTEGER,
            checkout_id INTEGER,
            source_url TEXT,
            browser_up TEXT,
            device_id INTEGER,
            referring_site TEXT,
            total_price INTEGER,
            name TEXT,
            checkout_token TEXT,
            created_at TIMESTAMP,
            filfillment_status TEXT,
            token TEXT,
            contact_email TEXT,
            order_status_url TEXT,
            order_number INTEGER
        )
        """,
        """
        CREATE TABLE line_items (
            order_id INTEGER,
            quantity INTEGER,
            product_id INTEGER,
            id INTEGER,
            variant_id INTEGER,
            FOREIGN KEY (order_id)
                REFERENCES orders (id)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
