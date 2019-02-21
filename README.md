# codingchallenge_datamigration

This coding challenge takes a set of data files called data.zip, copied from [this repo](https://github.com/Samariya57/coding_challenges/blob/master/data_migration.md).

## Purpose

This repo is designed to be an ETL (Extract, Transform, Load) pipeline for processing company orders and inserting them into SQL tables that can be used by business analysts. While only a small dataset was used, the goal is for the pipeline to be scalable, and for it to be able to add new orders over time.

## Pre-pipeline steps

**datamigration_db.ini**

Configuration file for the postgres database. The database must be created beforehand.

**datamigration_createtable.py**

The psycopg2 package was used to create two tables in the postgres database. The tables are orders and line_items, with columns corresponding to those found in the files in data.zip.

The column 'id' in the orders table was used as a key between the orders and line_items tables. Each order may contain multiple items, so this is a way to retrieve information about each item from the line_items table by order (id) in the orders table. In line_items, this is the order_id column.

## Schema:

    ORDERS:

        -column1
    
        -column2
    
        -id (PRIMARY KEY)
    
        -etc.
    
            LINE_ITEMS:
        
                -column1
            
                -column2
            
                -order_id (FOREIGN KEY)
            
                -etc.

## Pipeline:

**datamigration_run.sh**

A shell script that calls datamigration.py. Allows for variable inputs for the repo local path and the path for the data (also makes it flexible for inserting more data in the future).

**datamigration.py**

**unzip_data:** Loads and unzips the json files, where the input is the datapath from datamigration_run.sh

**orders_keylist:** Extracts the keys of the orders from the json dictionary. It also extracts the values of each key for each order.

**lineitems_keylist:** Extracts the keys of the line_items for each order from the json dictionary. It also extracts the values of each key for each item from each order.

**config:** Loads the postgres database information from the config file datamigration_db.ini.

**insert_orders:** Inserts the extracted orders and line_items information from the json dictionary. order_keys and lineitems_keys become the columns for the orders and line_items tables, respectively. order_vals and lineitems_vals become the row entries for each order and item in the orders and line_items tables, respectively.

