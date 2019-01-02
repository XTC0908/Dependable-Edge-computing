# This file is used to visualize the map.
# On the map, roads, edges (cars) and their conditions are included.
# For roads, "red" color represents jammed, while "green" color represents smooth.
# For edges, a dot of blue color represents a car. Every edge has a respective risk zone.
# Risk zone is a dash-line rectangle. "red" color represents in the edge is in risk, while "green" color safe.
# This file includes visualization functions and server building.
# The system which runs this file is a server to receive data from digital twin which updates object status. 

import tkinter as tk
import osmnx as ox
import sys
import math
from util import download_map
import socket
import ast
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import queue
from multiprocessing import Process
from threading import Thread
import sys
import os

# Following is the setting of server building

def ConstructHandler(message_queue, root):
    class PostHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.queue = message_queue
            self.root = root
            super(PostHandler, self).__init__(*args, **kwargs)

        def _set_response(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()

        def do_POST(self):
            length = int(self.headers['Content-Length'])
            self._set_response()
            raw_str = self.rfile.read(length)
            json_body = json.loads(raw_str)
            try:
                self.queue.put(json_body)
            except queue.Full:
                pass
            self.root.event_generate("<<new_post>>", when='tail')
    
    return PostHandler

def start_server(post_handler, address=('127.0.0.1', 8888)): # address can be adjusted due to different conditions
    print(os.getppid())
    httpd = HTTPServer(address, post_handler)
    #try:
    httpd.serve_forever()
    #except KeyboardInterrupt:
    #    pass
    #
    #httpd.server_close()


# RoadMap class supports the main object information storage and update.
class RoadMap(object):
    cars = []
    jam_edge = []
    smooth_edge = []
    safetyzone = []

    # initialization the class
    # define data framework
    def __init__(self, road_map=None):
        self.jam_edge = []
        self.smooth_edge = []
        self.cars = []
        self.safetyzone = []
        self.map = road_map
        if road_map != None:
            edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
            self.bbox = edges.total_bounds #west, south, east, north
        else:
            self.bbox = None

    # risk zone drawing function
    def draw_square(self, handler, dot_list, color):
        p = dot_list
        if color == 'red':
            color = '#E91822'
        else:
            color = '#29A71A'
        handler.create_line(p[0][0], p[0][1], p[1][0], p[1][1], width=5, fill=color, dash = 5)
        handler.create_line(p[2][0], p[2][1], p[1][0], p[1][1], width=5, fill=color, dash = 5)
        handler.create_line(p[0][0], p[0][1], p[3][0], p[3][1], width=5, fill=color, dash = 5)
        handler.create_line(p[2][0], p[2][1], p[3][0], p[3][1], width=5, fill=color, dash = 5)

    # draw roads which are jammed
    def draw_jammed_edge(self, handler):
        # red color
        G = self.map
        mapping = self.__mapping__(self.width, self.height) # a simpler form of mapping function, defined below
        for u, v in self.jam_edge:
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#F81818')

    # draw roads which are not jammed
    def draw_smooth_edge(self, handler):
        # green color
        G = self.map
        mapping = self.__mapping__(self.width, self.height)
        for u, v in self.smooth_edge:
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#07B123')
    
    # store map information
    def load_map(self, path):
        self.map = ox.load_graphml(path)
        edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
        self.bbox = edges.total_bounds #west, south, east, north

    # draw initial map roads with gray color
    def draw_map(self, handler): # handler -> canvas
        handler.delete('all') # clean canvas
        width, height = handler.winfo_width(), handler.winfo_height()
        self.width, self.height = width, height
        G = self.map
        mapping = self.__mapping__(width, height)
        
        for u, v in G.edges(keys=False, data=False):
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#B0B0B0') # gray color
            

    # update a jammed road information in map storage
    def input_jammed_node(self, ux, uy, vx, vy, color=None):
        # input: a node which is a part of a jammed edge
        # jammed_node: longitude and latitude, similar to G.nodes[u]['x'], G.nodes[u]['y'] in draw_map function
        # the jammed edge is added into self.smooth_edge (coordinates of canvas)
    
        print('####')
        u_red, v_red = ux, vx
        self.jam_edge.append((u_red, v_red))
        for u, v in self.smooth_edge:
            if u == u_red and v == v_red:
                self.smooth_edge.remove((u, v))

        
    # update a non-jammed road information in map storage
    def input_smooth_node(self, ux, uy, vx, vy):
        # input: a node which is a part of a jammed edge
        # jammed_node: longitude and latitude, similar to G.nodes[u]['x'], G.nodes[u]['y'] in draw_map function
        # the jammed edge is added into self.smooth_edge (coordinates of canvas)
        G = self.map
        u_red, v_red = 0, 0
        for u, v in G.edges(keys=False, data=False):
            if G.nodes[u]['x'] == ux and G.nodes[u]['y'] == uy and G.nodes[v]['x'] == vx and G.nodes[v]['y'] == vy:
                u_red, v_red = u, v 
                break  
            
        self.smooth_edge.append((u_red, v_red))
        for u, v in self.jam_edge:
            if u == u_red and v == v_red:
                self.jam_edge.remove((u, v))

    # update (add) car information in the map storage
    def input_cars(self, car_dic_element):
        # car_dic_element is a dic type element
        print('\n\nbefore input car  ', self.cars)
        if car_dic_element['category'] != 'car':
            return 
        ID, x, y = car_dic_element['id'], car_dic_element['x'], car_dic_element['y']
        newcar = {'id': ID, 'x': x, 'y': y}
        for c in self.cars:
            if c['id'] == ID:
                self.cars.remove(c) # check and remove old and redundant car information
                break
        self.cars.append(newcar)    
        print('\nafter input car  ', self.cars) # showing current car information

    # draw cars on the canvas
    def draw_cars(self, handler):
        # car_element is an element of self.car
        # draw cars
        G = self.map
        mapping = self.__mapping__(self.width, self.height)
        for c in self.cars:
            x, y = c['x'], c['y']
            x_1, y_1 = mapping(x, y)
            handler.create_oval(x_1 - 10, y_1 - 10, x_1 + 10, y_1 + 10, fill="#07C8C5")
            #light blue dot represent car

    # update safety zone information in the storage
    def input_safetyzone(self, sz_element):
        print('\n\nbefore input sftyz: ', self.safetyzone)
        mapping = self.__mapping__(self.width, self.height)
        ID, color = sz_element['id'], sz_element['color']
        dots = []
        x, y = mapping(sz_element['dot1'][0], sz_element['dot1'][1])
        dots.append([x, y])
        x, y = mapping(sz_element['dot2'][0], sz_element['dot2'][1])
        dots.append([x, y])
        x, y = mapping(sz_element['dot3'][0], sz_element['dot3'][1])
        dots.append([x, y])
        x, y = mapping(sz_element['dot4'][0], sz_element['dot4'][1])
        dots.append([x, y])
        sz = {'id': ID, 'dots': dots, 'color': color}
        for s in self.safetyzone:
            if s['id'] == ID:
                self.safetyzone.remove(s) # check and delete old and redundant safety zone
                break
        self.safetyzone.append(sz)
        print('\nafter input sftyz: ', self.safetyzone)
    
    # draw all safety zones 
    def draw_safetyzone(self, handler):
        for sz in self.safetyzone:
            dot = sz['dots']
            if sz['color'] == 'red':
                color = '#C70039' # red
            else:
                color = '#29A71A' # green
            print(dot)
            handler.create_line(dot[0][0], dot[0][1], dot[1][0], dot[1][1], width=8, fill=color, dash = 3)
            handler.create_line(dot[2][0], dot[2][1], dot[1][0], dot[1][1], width=8, fill=color, dash = 3)
            handler.create_line(dot[0][0], dot[0][1], dot[3][0], dot[3][1], width=8, fill=color, dash = 3)
            handler.create_line(dot[2][0], dot[2][1], dot[3][0], dot[3][1], width=8, fill=color, dash = 3)

    # define a mapping function
    def __mapping__(self, w, h):
        offset_x, offset_y = self.bbox[0], self.bbox[3]
        scale_x = w/(self.bbox[2] - self.bbox[0])
        scale_y = h/(self.bbox[1] - self.bbox[3])

        return lambda x, y: (int((x-offset_x)*scale_x), int((y-offset_y)*scale_y))

# initial canvas info
def init_canvas(master, width, height):
    canvas = tk.Canvas(master, width=width, height=height, bg='white')
    canvas.pack()
    master.update_idletasks()
    return canvas

# exit function
def close_window(event, server):
    server.join(timeout=0.1)
    sys.exit()

# receive message and update storage and refresh the canvas
def update_window(event, message, road_map, handler):
    try:
        # receive a new massage
        # check if it is legal
        # if legal, do respective command
        message_body = message.get(timeout=1)
        if message_body["category"] == 'car':
            road_map.input_cars(message_body)
        elif message_body["category"] == 'safetyzone':
            print('safetyzone receive')
            road_map.input_safetyzone(message_body)
        elif message_body["category"] == 'road':
            ux, uy = message_body["ux"], message_body["uy"]
            vx, vy = message_body["vx"], message_body["vy"]
            if message_body["state"] == 'smooth':
                road_map.input_smooth_node(ux, uy, vx, vy)
            elif message_body["state"] == 'jam':
                print(message_body)
                road_map.input_jammed_node(ux, uy, vx, vy)
            else:
                road_map.input_jammed_node(ux, uy, vx, vy, color='#00FFFF')
                    
        else:
            print('unknown message')
    except queue.Empty:
        print('queue is empty')

    # re-draw the map
    handler.delete('all')
    road_map.draw_map(handler)
    road_map.draw_jammed_edge(handler)
    road_map.draw_smooth_edge(handler)
    road_map.draw_cars(handler)
    road_map.draw_safetyzone(handler)

# main function to initialize the system and run it.
if __name__ == "__main__":
    print(os.getppid())

    message = queue.Queue()
    root = tk.Tk()

    post_handler = ConstructHandler(message, root)
    server =  Thread(target=start_server, args=(post_handler, ))
    server.setDaemon(True)
    server.start()
    

    road_map = RoadMap()
    road_map.load_map('demo.graphml')

    root.geometry('1500x1500')
    canvas = init_canvas(root, 1500, 1500)

    road_map.draw_map(canvas)

    close = lambda x:close_window(x, server)
    update = lambda x: update_window(x, message, road_map, canvas)

    root.bind('<Escape>', close)
    root.bind("<<new_post>>", update)
    root.mainloop()