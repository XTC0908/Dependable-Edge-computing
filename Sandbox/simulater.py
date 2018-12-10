import requests
import json
import time
#import utm
import numpy as np
import sys 
import copy
import threading
import queue
import websocket
sys.path.append("../rosws/")
from sub_client import monitorGeopoint
from pub_client import pubcmd

TCP_IP = '192.168.0.1'#130.229.153.146'
TCP_PORT = 9090
BUFFER_SIZE = 4096

WEBSOCKET_URL = "ws://"+TCP_IP+":"+str(TCP_PORT)
#toUtm = lambda x: np.array(utm.from_latlon(x[0], x[1])[:2])

class Vehicle(object):
    def __init__(self, sandbox_url, init):
        self.sandbox = sandbox_url
        self.info = init
        self.start_p = init['position']
        self.end_p = init['dest']
        self.count_len = 0
        self.queue = queue.Queue()

        r = requests.post(self.sandbox, data=json.dumps(init))
        
        self.action = list(json.loads(r.text))
        self.action[0][-2] = init['position']
        self.action[0][-1] = self.action[1][-2]
        self.action[-1][-2] = self.action[-2][-1]
        self.action[-1][-1] = init['dest']

        #sub_client = lambda x: monitorGeopoint(x)
        self.rcv_msg = threading.Thread(target = monitorGeopoint,args = (self.queue, ))
        self.rcv_msg.start()

        try:
          self.ws = websocket.create_connection(WEBSOCKET_URL)
          print("The connection to "+ WEBSOCKET_URL +" is successful!")
        except:
          print("The connection to "+ WEBSOCKET_URL +" fails!")

    
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

    def run_remote(self, jam):
        data = copy.deepcopy(self.info)
        
        for act in self.action:
            target = (1, 1, act[-1][0],act[-1][1] ,0.0)
            pubcmd(target, self.ws)
            while True:
                msg = self.queue.get()
                if abs(msg['msg']['geo']['latitude']-act[-1][0]) < 1e-8 \
                    and abs(msg['msg']['geo']['longitude']-act[-1][1]) <1e-8:
                    print('arrive', act[-1])
                    break
                
                data['u'] = None
                data['v'] = None
                data['sensor'] = 'smooth'
                data['position'] = [msg['msg']['geo']['latitude'], msg['msg']['geo']['longitude']]
                data['time_stamp'] = msg['msg']['header']['stamp']['nsecs']*1e-9
                data['type'] = 'pos'
                r = requests.post(self.sandbox, data=json.dumps(data))
                #print(act[-1])
                #print(msg)
                
            


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
    
    local = sys.argv[1]

    
    vid = sys.argv[2]
    direction = sys.argv[3]
    jam = sys.argv[4]
    if direction == "i":
        v1 = Vehicle('http://localhost:9000', \
                    {"type":"new", "vid": vid, "dest": [59.3365935,18.0674845], \
                     "position": [59.3428782,18.078231], "time_stamp": 0.000})
    else:
        v1 = Vehicle('http://localhost:9000', \
            {"type":"new", "vid": 1, "position": [59.3365935,18.0674845], \
             "dest": [59.3428782,18.078231], "time_stamp": 0.000})

    if local == 'local':
        v1.run(jam)
    elif local == 'remote':
        v1.run_remote(jam)

