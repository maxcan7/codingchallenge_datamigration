import json
import zipfile

d = None
data = None
with zipfile.ZipFile("C:/Users/maxca/Documents/GitHub/codingchallenge_datamigration/data.zip", "r") as z:
    for filename in z.namelist():
        print(filename)
    with z.open(filename) as f:
        data = f.read()
        d = json.loads(data.decode("utf-8"))
