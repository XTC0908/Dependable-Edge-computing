#!/usr/bin/env python

#import bson
import json
import time
import socket
import pprint
import websocket
import argparse
import threading
import sys
import queue
#args = parser.parse_args()

print("BSON-ROSBridge Testclient")

TCP_IP = '130.229.153.146'
TCP_PORT = 9090
BUFFER_SIZE = 4096

WEBSOCKET_URL = "ws://"+TCP_IP+":"+str(TCP_PORT)

TEST_MODE = "JSON"
COMMUNICATION_METHOD = "TCP"

def monitorGeopoint(msg_queue):
  geo_msg_info = {
    "op": "subscribe",
    "topic": "/geopoint",
    "type": "edge_info/vhc_geo"
  }
  try:
    ws = websocket.create_connection(WEBSOCKET_URL)
    print("The connection is successful!")
  except:
    print("The connection fails!")
  geo_info_json = json.dumps(geo_msg_info)
  ws.send(geo_info_json)
  while(1):
    rcv_json = ws.recv()
    type_msg = json.loads(rcv_json)['op']
    if type_msg == 'publish':
      msgs_conf = json.loads(rcv_json)
      dictionary = json.loads(rcv_json)#['msg']['geo']['latitude']
      try:
        msg_queue.put(dictionary)
      except:
        print('queue is full')

def monitorObs():
  obs_msg_info = {
    "op": "subscribe",
    "topic": "/obspoint",
    "type": "edge_info/vhc_geo"
  }
  try:
    obsws = websocket.create_connection(WEBSOCKET_URL)
    print("The connection is successful!")
  except:
    print("The connection fails!")
  
  obs_info_json = json.dumps(obs_msg_info)
  obsws.send(obs_info_json)
  while(1):
    obs_json = obsws.recv()
    type_msg = json.loads(obs_json)['op']
    if type_msg == 'publish':
      msgs_conf = json.loads(obs_json)
      dictionary = json.loads(obs_json)['msg']['geo']['latitude']
      print(dictionary)

#monitorGeopoint()

#T1 = threading.Thread(target = monitorGeopoint,args = ())
#T2 = threading.Thread(target = monitorObs,args = ())
#T1.start()
#T2.start()








