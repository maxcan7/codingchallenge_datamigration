#!/usr/bin/env bash
mainpath='C:/Users/maxca/Documents/GitHub/codingchallenge_datamigration/'
datapath='data/data.zip'
datapath=$mainpath$datapath
config='C:/Users/maxca/Documents/GitHub/codingchallenge_datamigration/database/datamigration_db.ini'
./src/datamigration.py $datapath $config
