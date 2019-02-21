#!/usr/bin/env bash

mainpath='/home/ubuntu/codingchallenge_datamigration/'
datapath='data/data.zip'
datapath=$mainpath$datapath
./datamigration.py $datapath
