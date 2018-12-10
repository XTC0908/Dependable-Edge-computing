#!/usr/bin/env python

#import bson
import json
import time
import socket
import pprint
import websocket
import argparse

TCP_IP = '192.168.0.1'#'130.229.153.146'
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
