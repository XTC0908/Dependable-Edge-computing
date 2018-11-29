import requests
import time

headers = {'Content-type': 'application/json'}

data1 =  '{"category": "car", "id": 1, "x": 333307.4094043318, "y": 6581667.751225858}'
data2 =  '{"category": "car", "id": 1, "x": 333294.50284388475, "y": 6581655.340821373}'

while 1:
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=data1)
    time.sleep(2)
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=data2)
    time.sleep(2)