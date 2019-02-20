#!/usr/bin/env python
import json
import zipfile
import sys

# Import path from shell script
mainpath = sys.argv[1]

# Initialize variables
d = None
data = None
# Unzip and open json files
with zipfile.ZipFile(mainpath+"data.zip", "r") as z:
    for filename in z.namelist():
        print(filename)
    with z.open(filename) as f:
        data = f.read()
        d = json.loads(data.decode("utf-8"))
