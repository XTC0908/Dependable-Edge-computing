import requests
import json

class InterfaceViz(object):
    def __init__(self, url):
        self.car_body = {
                        "category": "car",
                        "id": None,
                        "x": None,
                        "y": None
                    }
        self.risk_zone_body = {
                                "category": "safetyzone", 
                                "id": None, 
                                "x": None, 
                                "y": None, 
                                "dot1": None, 
                                "dot2": None, 
                                "dot3": None, 
                                "dot4": None, 
                                "color": "#162C22"
                                }
        self.road_body = {
                                "category": "road", 
                                "ux": None, 
                                "uy": None,
                                "vx": None,
                                "vy": None, 
                                "state": "jam"
                            }
        self.url = url

    def car_req(self, data):
        body = self.car_body.copy()
        body['id'] = data['id']
        body['x'] = data['x']
        body['y'] = data['y']
        r = requests.post(self.url, data=json.dumps(body))
        return r


    def risk_zone_req(self, data):
        body = self.risk_zone_body.copy()
        body['id'] = data['id']
        body['x'] = data['x']
        body['y'] = data['y']
        body['dot1'] = data['dot1']
        body['dot2'] = data['dot2']
        body['dot3'] = data['dot3']
        body['dot4'] = data['dot4']
        r = requests.post(self.url, data=json.dumps(body))
        return r

    def road_req(self, data):
        body = self.road_body.copy()
        body['id'] = data['id']
        body['state'] = data['state']
        body['ux'] = data['ux']
        body['uy'] = data['uy']
        body['vx'] = data['vx']
        body['vy'] = data['vy']
        r = requests.post(self.url, data=json.dumps(body))
        return r


if __name__=='__main__':
    viz = InterfaceViz('http://localhost:8888')
    r = viz.car_req({'id':3, 'x':12345, 'y':12345})
    r = viz.risk_zone_req({'id':3, 'x':12345, 'y':12345, 'dot1':1024, 'dot2':1024, 'dot3':1024, 'dot4':1024})
    r = viz.road_req({'id':3, 'ux':12345, 'uy':12345, 'vx':1092374, 'vy':32489938, 'state':123456})
    print(r.text)