import requests
import time

headers = {'Content-type': 'application/json'}

data1 =  '{"category": "car", "id": 1, "x": 333307.4094043318, "y": 6581667.751225858}'
data2 =  '{"category": "car", "id": 1, "x": 333294.50284388475, "y": 6581655.340821373}'
sz1 = '{"category": "safetyzone", "id": 1, "x": 333307.4094043318, "y": 6581667.751225858, "dot1": [333320, 6581560], "dot2": [333307, 6581560], "dot3": [333307, 6581670], "dot4": [333320, 6581670], "color": "red"}'
sz2 = '{"category": "safetyzone", "id": 1, "x": 333307.4094043318, "y": 6581667.751225858, "dot1": [333320, 6581560], "dot2": [333307, 6581560], "dot3": [333307, 6581670], "dot4": [333320, 6581670], "color": "green"}'
rd1 = '{"category": "road", "ux": 333829.31616017665, "uy":6581603.344312442,"vx": 333829.8199573766, "vy": 6581607.035191915, "state": "jam"}' # "jam" or "smooth"
rd2 = '{"category": "road", "ux": 333829.31616017665, "uy":6581603.344312442,"vx": 333829.8199573766, "vy": 6581607.035191915, "state": "smooth"}' # "jam" or "smooth"


while 1:
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=data1)
    time.sleep(2)
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=sz1)
    time.sleep(2)
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=rd1)
    time.sleep(2)
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=data2)
    time.sleep(2)
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=sz2)
    time.sleep(2)
    response = requests.post('http://127.0.0.1:8888', headers=headers, data=rd2)
    time.sleep(2)