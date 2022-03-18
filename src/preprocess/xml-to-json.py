"""
Converts all the xml_files in xml_dir into json files and saves them in a new subfolder
"""

import json
import xmltodict
from os import listdir
from os.path import isfile, join

xml_dir = "data/MakeML/annotations"
json_dir = "data/MakeML/json"

xml_files = [f for f in listdir(xml_dir) if isfile(join(xml_dir, f))]

for file in xml_files:
    data_dict = {}
    json_file_name = file[:file.rfind('.')] + ".json"

    print(f"Converting {file} to {json_file_name}...")

    # Read xml data
    with open(join(xml_dir, file)) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()

    # Write json data
    json_data = json.dumps(data_dict)
    with open(join(json_dir, json_file_name), "w") as json_file:
        json_file.write(json_data)
    json_file.close()


print(f"\nSuccessfully converted {len(xml_files)} files and saved them in {xml_dir}/json")