#!/usr/bin/env bash
mainpath='path'
datapath='data/data.zip'
datapath=$mainpath$datapath
config='inifile path'
./src/datamigration.py $datapath $config