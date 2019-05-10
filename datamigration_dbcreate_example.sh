#!/usr/bin/env bash

postgresuser='postgres'
postgreshost='localhost'
db_password='****'
./src/datamigration.py $postgresuser $postgreshost $db_password