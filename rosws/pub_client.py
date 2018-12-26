#!/usr/bin/env python

<<<<<<< HEAD
import bson
=======
#import bson
>>>>>>> 549e3cec5b5c5d42ec123284b367be634d563b72
import json
import time
import socket
import pprint
import websocket
import argparse

<<<<<<< HEAD
TCP_IP = '127.0.0.1'
=======
TCP_IP = '192.168.0.1'#'130.229.153.146'
>>>>>>> 549e3cec5b5c5d42ec123284b367be634d563b72
TCP_PORT = 9090
BUFFER_SIZE = 4096

WEBSOCKET_URL = "ws://"+TCP_IP+":"+str(TCP_PORT)


def cmdFunction(vhcid,cmd):
  cmd_message = {
    "vhcid" : vhcid,
    "cmd" : cmd
  }
  return cmd_message

def setDest(vhcid,lat,lon,alt):
  vhcid = vhcid
  dest_message = {
    "vhcid" : vhcid,
    "geo" : { "latitude" : lat,
              "longitude" : lon,
              "altitude" : alt
    }
  }
  return dest_message

<<<<<<< HEAD
def pubcmd():
  try:
    ws = websocket.create_connection(WEBSOCKET_URL)
    print("The connection to "+ WEBSOCKET_URL +" is successful!")
  except:
    print("The connection to "+ WEBSOCKET_URL +" fails!")


  while(1):

    vhc,cmd,lat,lon,alt= raw_input("[vhcid cmd lat lon alt]]\n").split()
    my_cmd = cmdFunction(int(vhc),int(cmd))
    path_cmd = setDest(int(vhc),float(lat),float(lon),float(alt))

    cmd_msg_info = {
      "op": "publish",
      "topic": "/vhc_status_m",
      "type": "edge_info/vhc_cmd",
      "msg" : my_cmd
    }
    
    path_msg_info = {
      "op": "publish",
      "topic": "/vhc_path_msg",
      "type": "edge_info/vhc_geo",
      "msg" : path_cmd
    }

    if cmd == '1' or cmd == '0':
      cmd_info_json = json.dumps(cmd_msg_info)
      ws.send(cmd_info_json)
      print("command sent")
    elif cmd == '2':
      path_info_json = json.dumps(path_msg_info)
      ws.send(path_info_json)
      print("command sent")

pubcmd()
=======
def pubcmd(target, ws):

  #while(1):
    #vhc = input("Which vehicle? ")
    #cmd = input("Input 1 to start, input 0 to stop:")

  vhc,cmd,lat,lon,alt = target #input("[vhcid cmd lat lon alt]]\n").split()
  my_cmd = cmdFunction(int(vhc),int(cmd))
  path_cmd = setDest(int(vhc),float(lat),float(lon),float(alt))
  cmd_msg_info = {
    "op": "publish",
    "topic": "/vhc_status_m",
    "type": "edge_info/vhc_cmd",
    "msg" : my_cmd
  }
  
  path_msg_info = {
    "op": "publish",
    "topic": "/vhc_path_msg",
    "type": "edge_info/vhc_geo",
    "msg" : path_cmd
  }
  cmd_info_json = json.dumps(cmd_msg_info)
  ws.send(cmd_info_json)
  path_info_json = json.dumps(path_msg_info)
  ws.send(path_info_json)

#pubcmd()
>>>>>>> 549e3cec5b5c5d42ec123284b367be634d563b72
