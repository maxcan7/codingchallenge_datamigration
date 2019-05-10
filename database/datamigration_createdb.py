#!/usr/bin/env py

from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = None
con = connect(dbname='postgres', user=sys.argv[1], host=sys.argv[2],
              password=sys.argv[3])

newdb = "datamigration_db"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE ' + newdb)
cur.close()
con.close()
