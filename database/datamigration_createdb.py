#!/usr/bin/env py

from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = connect(database=sys.argv[1], port=sys.argv[2], user=sys.argv[3],
              password=sys.argv[4], host=sys.argv[5])

newdb = "datamigration_db"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE %s ;' % newdb)
cur.close()
con.close()
