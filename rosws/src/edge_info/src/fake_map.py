import json
json_data = []
with open('map_node.json') as json_file:
    json_data = json.load(json_file)
for item in json_data:
    for data_item in item['lon']:
        print data_item
