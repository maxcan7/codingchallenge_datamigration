#!/usr/bin/env python
import json
import zipfile
import sys
import psycopg2
from configparser import ConfigParser


# Unzip
def unzip_data(datapath=sys.argv[1]):
    # Initialize variables
    d = None
    data = None
    # Unzip and open json files
    with zipfile.ZipFile(datapath, "r") as z:
        for filename in z.namelist():
            print(filename)
        with z.open(filename) as f:
            data = f.read()
            d = json.loads(data.decode("utf-8"))
    return d


# Load config file for database
def config(filename='datamigration_db.ini', section='postgresql'):
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


if __name__ == '__main__':
    unzip_data()
