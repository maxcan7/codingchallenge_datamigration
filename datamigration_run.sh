#!/usr/bin/env bash

mainpath='/home/ubuntu/codingchallenge_datamigration/'
datapath='data/data.zip'
datapath=$mainpath$datapath
./src/datamigration.py $datapath
