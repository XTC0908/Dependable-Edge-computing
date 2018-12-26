#!/usr/bin/env python

import bson
import json
import time
import socket
import pprint
import websocket
import argparse
import threading
import sys
import pygame

#args = parser.parse_args()

print("BSON-ROSBridge Testclient")

TCP_IP = '127.0.0.1'
TCP_PORT = 9090
BUFFER_SIZE = 4096

WEBSOCKET_URL = "ws://"+TCP_IP+":"+str(TCP_PORT)

TEST_MODE = "JSON"
COMMUNICATION_METHOD = "TCP"

def monitorGeopoint():
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



  WINSIZE = [200, 200]
  pygame.init()
  screen = pygame.display.set_mode(WINSIZE)

  pygame.display.set_caption('visualization')
  yellow = 255, 240, 200
  black = 20, 20, 40
  screen.fill((100, 100, 100))
  zerolat = 59.33659
  zerolon = 18.06748

  geo_info_json = json.dumps(geo_msg_info)
  ws.send(geo_info_json)
  while(1):
    rcv_json = ws.recv()
    type_msg = json.loads(rcv_json)['op']
    if type_msg == 'publish':
      msgs_conf = json.loads(rcv_json)
      dictionary = json.loads(rcv_json)['msg']['geo']['latitude']
      lat = (json.loads(rcv_json)['msg']['geo']['latitude']-zerolat)*10000000
      lon = (json.loads(rcv_json)['msg']['geo']['longitude']-zerolon)*10000000
      print(lat)
      print(lon)
      pygame.draw.circle(screen, yellow, [int(lat),int(lon)], 5)
      pygame.display.update()

def monitorObs():
  obs_msg_info = {
    "op": "subscribe",
    "topic": "/obspoint",
    "type": "edge_info/vhc_geo"
  }




  WINSIZE = [200, 200]
  pygame.init()
  screen = pygame.display.set_mode(WINSIZE)

  pygame.display.set_caption('visualization')
  yellow = 255, 240, 200
  black = 20, 20, 40
  screen.fill((100, 100, 100))
  zerolat = 59.33659
  zerolon = 18.06748
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
      dictionary = json.loads(obs_json)['msg']['geo']['latitude']
      lat = (json.loads(obs_json)['msg']['geo']['latitude']-zerolat)*1000000
      lon = (json.loads(obs_json)['msg']['geo']['longitude']-zerolon)*1000000
      print(lat)
      print(lon)
      pygame.draw.circle(screen, green, [int(lat),int(lon)], 5)
      pygame.update()

monitorGeopoint()

T1 = threading.Thread(target = monitorGeopoint,args = ())
T2 = threading.Thread(target = monitorObs,args = ())
T1.start()
T2.start()





