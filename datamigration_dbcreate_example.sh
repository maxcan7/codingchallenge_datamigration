#!/usr/bin/env bash

defaultdb='postgres'
port=5432
user='postgres'
password='****'
host='localhost'
./database/datamigration_createdb.py $defaultdb $port $user $password $host