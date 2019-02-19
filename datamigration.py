import json
import zipfile

d = None
data = None
with zipfile.ZipFile("./data/drug-event-Q4-0001-of-0013.json.zip", "r") as z:
    for filename in z.namelist():
        print(filename)
    with z.open(filename) as f:
        data = f.read()
        d = json.loads(data.decode("utf-8"))
