import requests
import json
import time
import utm
import numpy as np
import sys 
import copy


toUtm = lambda x: np.array(utm.from_latlon(x[0], x[1])[:2])

class Vehicle(object):
    def __init__(self, sandbox_url, init):
        self.sandbox = sandbox_url
        self.info = init
        self.start_p = init['position']
        self.end_p = init['dest']
        self.count_len = 0

        r = requests.post(self.sandbox, data=json.dumps(init))
        
        self.action = list(json.loads(r.text))
        self.action[0][-2] = init['position']
        self.action[0][-1] = self.action[1][-2]
        self.action[-1][-2] = self.action[-2][-1]
        self.action[-1][-1] = init['dest']        

    
    def run(self, jam):

        norm = lambda x: np.sqrt(np.sum(x**2))
        data = copy.deepcopy(self.info)
        for i in range(200):
            time.sleep(0.2)
        
            if i != 88 or jam != 'jam':
                pos, _, _ = self.step()
                #print(idx, self.count_len, list(next_point+np.floor(b)), path_len, length)
                data['u'] = None
                data['v'] = None
                data['sensor'] = 'smooth'
            else:
                pos, u, v = self.step()
                data['u'] = u
                data['v'] = v
                data['sensor'] = 'jam'
        
            data['position'] = list(pos)
            data['time_stamp'] = 0.25*i
            data['type'] = 'pos'
            r = requests.post(self.sandbox, data=json.dumps(data))

    def step(self):
        way_point = np.array([self.action[i][-2:] for i in range(len(self.action))]) - [59, 18]
        dist = np.sum((way_point[:, 1, :] - way_point[:, 0, :])**2, axis=1)**0.5
        
        full_length = np.sum(dist)
        step_len = full_length/200

        self.count_len += step_len


        start = None
        res = None
        l = self.count_len

        for i, d in enumerate(dist):
            l -= d
            if l <= 0:
                path = way_point[i]
                l_path = dist[i]
                res = l + d
                u, v = self.action[i][1], self.action[i][2]
                break
        
        direction = path[1] - path[0]
        d = direction*(res/l_path) + path[0]
        
        return d+[59, 18], u, v


if __name__=='__main__':
    
    vid = sys.argv[1]
    direction = sys.argv[2]
    jam = sys.argv[3]

    if direction == "i":
        v1 = Vehicle('http://localhost:9000', \
                    {"type":"new", "vid": vid, "dest": [59.3365935,18.0674845], \
                     "position": [59.3428782,18.078231], "time_stamp": 0.000})

    else:
        v1 = Vehicle('http://localhost:9000', \
            {"type":"new", "vid": 1, "position": [59.3365935,18.0674845], \
             "dest": [59.3428782,18.078231], "time_stamp": 0.000})


    v1.run(jam)
