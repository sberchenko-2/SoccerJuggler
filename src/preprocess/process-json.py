"""
Process MakeML json data into a single file
"""

import json
from os import listdir
from os.path import isfile, join

json_dir = "data/MakeML/json"
output_file = "data/MakeML/bndboxes.json"

json_files = [f for f in listdir(json_dir) if isfile(join(json_dir, f))]

data = []
for file in json_files:
    print(f"Reading data from {file}...")

    with open(join(json_dir, file)) as json_file:
        json_data = json.load(json_file)
        data.append(json_data['annotation']['object']['bndbox'])

# Write json data
json_data = json.dumps(data)
with open(output_file, "w") as json_file:
    json_file.write(json_data)
json_file.close()