#!/usr/bin/env bash

mainpath='/c/Users/maxca/Documents/GitHub/codingchallenge_datamigration'
datapath='data/data.zip'
datapath=$mainpath$datapath
./src/datamigration.py $datapath
