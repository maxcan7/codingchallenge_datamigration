#!/usr/bin/env py
import json
import zipfile
import sys
import psycopg2
from configparser import ConfigParser


# Get filelist
def get_filelist(datapath=sys.argv[1]):
    with zipfile.ZipFile(datapath, "r") as z:
        filelist = z.namelist()
    return filelist


# Load data
def unzip_data(datapath, file):
    # Initialize variables
    d = None
    data = None
    # Unzip and open json files
    with zipfile.ZipFile(datapath, "r") as z:
        with z.open(file) as f:
            data = f.read()
            d = json.loads(data.decode("utf-8"))
    return d


# Get keylist for orders table
def orders_keylist(d):
    # The json data is a dictionary with key 'orders' and value being
    # a dictionary for that order. We need to extract the keys from
    # one of those orders.
    orderkeys = [key for key in d['orders'][0].keys() if key != 'line_items']
    # Likewise, we need to extract the values of each order for each key,
    # besides line_items, since that is also a value that is a separate
    # dictionary, and will go into its own table.
    idx = 0
    # For each order
    for order in d['orders']:
        # Get values for each key besides line_items
        if idx == 0:
            ordervals = [[val for val in d['orders'][idx].values()
                         if d['orders'][idx].keys() != 'line_items']]
            idx += 1
        else:
            ordervals.append([val for val in d['orders'][idx].values()
                             if d['orders'][idx].keys() != 'line_items']
                             )
            idx += 1

    return (orderkeys, ordervals)


# Get keylist for line_items table
def lineitems_keylist(d):
    # Essentially the same logic as in the comments for def orders_kelist
    lineitems_keys = ['order_id'] + \
                [key for key in d['orders'][0]['line_items'][0].keys()]
    idx = 0
    for order in d['orders']:
        if idx == 0:
            lineitems_vals = [order['id']] + \
                [val for val in order['line_items'][0].values()]
            idx += 1
        else:
            lineitems_vals.append([order['id']] +
                                  [val for val in order['line_items'][0]
                                  .values()])
    return (lineitems_keys, lineitems_vals)


# Load config file for database
def config(filename=sys.argv[2], section='postgresql'):
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


# Insert data into postgres database tables
def insert_orders(tablename, keys, values):
    # Loop through each column
    for i in range(len(keys)):
        # Subset values to just values corresponding to i
        ival = [v[i] for v in values]
        # Create list of columns and values by key:values
        sql = "INSERT INTO %s(%s) VALUES(%s)"
        conn = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement with the inputted
            # tablename, the ith key, and all order values
            # for the ith key
            cur.executemany(sql, [tablename, keys[i], ival])
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    filelist = get_filelist()
    for file in filelist:
        d = unzip_data(sys.argv[1], file)
        [orderkeys, ordervals] = orders_keylist(d)
        [lineitems_keys, lineitems_vals] = lineitems_keylist(d)
        insert_orders('orders', orderkeys, ordervals)
        insert_orders('line_items', lineitems_keys, lineitems_vals)
