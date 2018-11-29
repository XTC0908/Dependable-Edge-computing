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

request = 'can you hear me?'
car_request = '{"category": "car", "id": 1, "x": 333307.4094043318, "y": 6581667.751225858}'
safety_zone_request = '{"category": "safetyzone", "id": 1, "x": 333307.4094043318, "y": 6581667.751225858, \
"dot1": (333320, 6581560), "dot2": (333307, 6581560), "dot3": (333307, 6581670), \
"dot4": (333320, 6581670), "color": "#162C22"}'
road_request = '{"category": "road", "ux": 333307.4094043318, "uy":6581667.751225858,\
"vx": 333294.50284388475, "vy": 6581655.340821373, "state": "jam"}' # "jam" or "smooth"


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

def start_server(post_handler, address=('127.0.0.1', 8888)):
    print(os.getppid())
    httpd = HTTPServer(address, post_handler)
    #try:
    httpd.serve_forever()
    #except KeyboardInterrupt:
    #    pass
    #
    #httpd.server_close()


class RoadMap(object):
    
    cars = []
    jam_edge = []
    smooth_edge = []
    safetyzone = []

    def __init__(self, road_map=None):
        self.jam_edge = []
        self.smooth_edge = []
        self.cars = []
        #self.cars = [{"id": 1, "x": 333307.4094043318, "y": 6581667.751225858},\
        #    {"id": 2, "x": 333307, "y": 6581560}]
        self.safetyzone = []
        self.map = road_map
        if road_map != None:
            edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
            self.bbox = edges.total_bounds #west, south, east, north
        else:
            self.bbox = None
        
    #def rotate(self, angle, center):
    #    angle = math.radians(angle)
    #    cos_val = math.cos(angle)
    #    sin_val = math.sin(angle)
    #    cx, cy = center
    #    new_points = []
    #    for x_old, y_old in self.rectangle_points:
    #        x_old -= cx
    #        y_old -= cy
    #        x_new = x_old * cos_val - y_old * sin_val
    #        y_new = x_old * sin_val + y_old * cos_val
    #        new_points.append([x_new + cx, y_new + cy])
    #    self.rotate_rectangle = new_points

    def draw_square(self, handler, dot_list, color):
        #p = self.rotate_rectangle
        p = dot_list
        if color == 'red':
            color = '#E91822'
        else:
            color = '#29A71A'
        handler.create_line(p[0][0], p[0][1], p[1][0], p[1][1], width=3, fill=color, dash = 5)
        handler.create_line(p[2][0], p[2][1], p[1][0], p[1][1], width=3, fill=color, dash = 5)
        handler.create_line(p[0][0], p[0][1], p[3][0], p[3][1], width=3, fill=color, dash = 5)
        handler.create_line(p[2][0], p[2][1], p[3][0], p[3][1], width=3, fill=color, dash = 5)

    def draw_jammed_edge(self, handler):
        # red color
        mapping = self.__mapping__(self.width, self.height)
        for u, v in self.jam_edge:
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#F81818')

    def draw_smooth_edge(self, handler):
        # green color
        mapping = self.__mapping__(self.width, self.height)
        for u, v in self.smooth_edge:
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#07B123')
    
    def load_map(self, path):
        self.map = ox.load_graphml(path)
        edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
        self.bbox = edges.total_bounds #west, south, east, north

    def draw_map(self, handler): # handler -> canvas
        handler.delete('all')
        width, height = handler.winfo_width(), handler.winfo_height()
        self.width, self.height = width, height
        G = self.map
        mapping = self.__mapping__(width, height)

        #print(G.edges(keys=False, data=False))
        
        for u, v in G.edges(keys=False, data=False):
            #print(G.nodes[u])
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#B0B0B0')
            
        for u, v in self.jam_edge:
            self.draw_jammed_edge(u, v, handler)


    def input_jammed_node(self, ux, uy, vx, vy, handler):
        # input: a node which is a part of a jammed edge
        # jammed_node: longitude and latitude, similar to G.nodes[u]['x'], G.nodes[u]['y'] in draw_map function
        # the jammed edge is added into self.smooth_edge (coordinates of canvas)
        G = self.map

        for u, v in G.edges(keys=False, data=False):
            if G.nodes[u]['x'] == ux and G.nodes[u]['y'] == uy and G.nodes[v]['x'] == vx and G.nodes[v]['y'] == vy:
                u_red, v_red = u, v 
                break  
        self.jam_edge.append((u_red, v_red))
        for u, v in self.smooth_edge:
            if u == u_red and v == v_red:
                self.smooth_edge.remove((u, v))

        for u, v in self.jam_edge:
            self.draw_jammed_edge(u, v, handler)

    def input_smooth_node(self, ux, uy, vx, vy, handler):
        # input: a node which is a part of a jammed edge
        # jammed_node: longitude and latitude, similar to G.nodes[u]['x'], G.nodes[u]['y'] in draw_map function
        # the jammed edge is added into self.smooth_edge (coordinates of canvas)
        G = self.map

        for u, v in G.edges(keys=False, data=False):
            if G.nodes[u]['x'] == ux and G.nodes[u]['y'] == uy and G.nodes[v]['x'] == vx and G.nodes[v]['y'] == vy:
                u_red, v_red = u, v 
                break  
            
        self.smooth_edge.append((u_red, v_red))
        for u, v in self.jam_edge:
            if u == u_red and v == v_red:
                self.jam_edge.remove((u, v))

        for u, v in self.smooth_edge:
            self.draw_smooth_edge(u, v, handler)

    def input_cars(self, car_dic_element):
        # car_dic_element is a dic type element
        print('\n\nbefore input car  ', self.cars)
        if car_dic_element['category'] != 'car':
            return 
        ID, x, y = car_dic_element['id'], car_dic_element['x'], car_dic_element['y']
        newcar = {'id': ID, 'x': x, 'y': y}
        for c in self.cars:
            if c['id'] == ID:
                self.cars.remove(c)
                break
        self.cars.append(newcar)    
        print('\nafter input car  ', self.cars)

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

    def input_safetyzone(self, sz_element):
        if sz_element['category'] is not 'safetyzone':
            return
        ID, color = sz_element['id'], sz_element['color']
        dots = []
        dots.append(sz_element['dot1'])
        dots.append(sz_element['dot2'])
        dots.append(sz_element['dot3'])
        dots.append(sz_element['dot4'])
        sz = {'id': ID, 'dots': dots, 'color': color}
        for s in self.safetyzone:
            if s['id'] == ID:
                self.safetyzone.remove(s)
                break
        self.safetyzone.append(sz)

    def draw_safetyzone(self, handler):
        G = self.map
        mapping = self.__mapping__(self.width, self.height)
        for sz in self.safetyzone:
            dot = sz['dots']
            if color == 'red':
                color = '#E91822'
            else:
                color = '#29A71A'
            handler.create_line(dot[0][0], dot[0][1], dot[1][0], dot[1][1], width=3, fill=color, dash = 5)
            handler.create_line(dot[2][0], dot[2][1], dot[1][0], dot[1][1], width=3, fill=color, dash = 5)
            handler.create_line(dot[0][0], dot[0][1], dot[3][0], dot[3][1], width=3, fill=color, dash = 5)
            handler.create_line(dot[2][0], dot[2][1], dot[3][0], dot[3][1], width=3, fill=color, dash = 5)

    def __mapping__(self, w, h):
        offset_x, offset_y = self.bbox[0], self.bbox[3]
        scale_x = w/(self.bbox[2] - self.bbox[0])
        scale_y = h/(self.bbox[1] - self.bbox[3])

        return lambda x, y: (int((x-offset_x)*scale_x), int((y-offset_y)*scale_y))


def init_canvas(master, width, height):
    canvas = tk.Canvas(master, width=width, height=height, bg='white')
    canvas.pack()
    master.update_idletasks()
    return canvas

#def receive_data(road_map, s, handler):
#
#    # accept and establish connection
#    conn, addr = s.accept()
#    # receive message
#    request    = conn.recv(1024).decode('utf-8')
# 
#    print('request is: ',request)
#    print('Connected by', addr)
#    # send message
#    reply = 'Yes : '
#    conn.sendall(reply.encode('utf-8'))
#    
#    #recv_dic = json.loads(request)
#    recv_dic = ast.literal_eval(request)
#    if recv_dic['category'] == 'safetyzone':
#        print(recv_dic['id'])
#
#    #testing
#    G = road_map.map
#    mapping = road_map.__mapping__(road_map.width, road_map.height)
#    
#    for x, y in road_map.cars:
#        x_1, y_1 = mapping(x, y)
#        handler.create_oval(x_1 - 10, y_1 - 10, x_1 + 10, y_1 + 10, fill='#FFFFBF')
#    #end of testing
#    root.after(3500, receive_data, road_map, s, handler)

def close_window(event, server):
    server.join(timeout=0.1)
    sys.exit()

def update_window(event, message, road_map, handler):
    try:
        message_body = message.get(timeout=1)
        if message_body["category"] == 'car':
            road_map.input_cars(message_body)
        elif message_body["category"] == 'safetyzone':
            road_map.input_safetyzone(message_body)
        elif message_body["category"] == 'road':
            ux, uy = message_body["ux"], message_body["uy"]
            vx, vy = message_body["vx"], message_body["vy"]
            if message_body["color"] != 'red':
                road_map.input_smooth_node(ux, uy, vx, vy)
            else:
                road_map.input_jammed_node(ux, uy, vx, vy)
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