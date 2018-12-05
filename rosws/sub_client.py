#!/usr/bin/env python

import bson
import json
import time
import socket
import pprint
import websocket
import argparse


#args = parser.parse_args()

print("BSON-ROSBridge Testclient")

TCP_IP = '127.0.0.1'
TCP_PORT = 9090
BUFFER_SIZE = 4096

WEBSOCKET_URL = "ws://"+TCP_IP+":"+str(TCP_PORT)

TEST_MODE = "JSON"
COMMUNICATION_METHOD = "TCP"

def cmdFunction(vhcid,cmd):
  vhcid = vhcid
  cmd_message = {
    "vhcid" : vhcid,
    "cmd" : cmd
  }
  return cmd_message


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
  print(type_msg)
  if type_msg == 'publish':
    msgs_conf = json.loads(rcv_json)
    dictionary = json.loads(rcv_json)['msg']['geo']['latitude']
    print(dictionary)




