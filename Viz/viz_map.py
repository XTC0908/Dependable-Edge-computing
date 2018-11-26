import tkinter as tk
import osmnx as ox
import sys
import math
from util import download_map
import requests

#simulated jammed edge
#jam_edge = [(1525463170, 222112985), (1525463170, 1525463175)]

class RoadMap(object):

    jam_edge = []
    smooth_edge = []
    cars = []

    rectangle_points = [(400, 400), (800, 400), (800, 600), (400, 600)]
    rotate_rectangle = []


    def __init__(self, road_map=None):
        self.map = road_map
        if road_map != None:
            edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
            self.bbox = edges.total_bounds #west, south, east, north
        else:
            self.bbox = None
        
    def rotate(self, angle, center):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in self.rectangle_points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        self.rotate_rectangle = new_points

    def draw_square(self, handler):
        p = self.rotate_rectangle
        handler.create_line(p[0][0], p[0][1], p[1][0], p[1][1], width=3, fill='yellow', dash = 5)
        handler.create_line(p[2][0], p[2][1], p[1][0], p[1][1], width=3, fill='yellow', dash = 5)
        handler.create_line(p[0][0], p[0][1], p[3][0], p[3][1], width=3, fill='yellow', dash = 5)
        handler.create_line(p[2][0], p[2][1], p[3][0], p[3][1], width=3, fill='yellow', dash = 5)

    def draw_jammed_edge(self, u, v, handler):
        # red color
        mapping = self.__mapping__(self.width, self.height)
        x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
        x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
        handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#F81818')

    def draw_smooth_edge(self, u, v, handler):
        # green color
        mapping = self.__mapping__(self.width, self.height)
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

        print(G.edges(keys=False, data=False))
        
        for u, v in G.edges(keys=False, data=False):
            #print(u, v)
            print(G.nodes[u])
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=10, fill='#B0B0B0')
            
        for u, v in self.jam_edge:
            self.draw_jammed_edge(u, v)


    def input_jammed_node(self, jammed_node_x, jammed_node_y, handler):
        # input: a node which is a part of a jammed edge
        # jammed_node: longitude and latitude, similar to G.nodes[u]['x'], G.nodes[u]['y'] in draw_map function
        # the jammed edge is added into self.smooth_edge (coordinates of canvas)
        G = self.map
        mapping = self.__mapping__(self.width, self.height)

        distance = 250000000
        x_0, y_0 = mapping(jammed_node_x, jammed_node_y)
        u_red, v_red = 0, 0 
        for u, v in G.edges(keys=False, data=False):
            ux, uy = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            distance_new = (ux - x_0) * (ux - x_0) + (uy - y_0) * (uy - y_0)
            if (distance_new < distance): 
                distance = distance_new
                u_red, v_red = u, v
        self.jam_edge.append((u_red, v_red))

        for u, v in self.jam_edge:
            self.draw_jammed_edge(u, v, handler)

    def input_smooth_node(self, smooth_node_x, smooth_node_y, handler):
        # input: a node which is a part of a jammed edge
        # jammed_node: longitude and latitude, similar to G.nodes[u]['x'], G.nodes[u]['y'] in draw_map function
        # the jammed edge is added into self.smooth_edge (coordinates of canvas)
        G = self.map
        mapping = self.__mapping__(self.width, self.height)

        distance = 250000000
        x_0, y_0 = mapping(smooth_node_x, smooth_node_y)
        u_green, v_green = 0, 0 
        for u, v in G.edges(keys=False, data=False):
            ux, uy = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            distance_new = (ux - x_0) * (ux - x_0) + (uy - y_0) * (uy - y_0)
            if (distance_new < distance): 
                distance = distance_new
                u_green, v_green = u, v
        self.smooth_edge.append((u_green, v_green))

        for u, v in self.smooth_edge:
            self.draw_smooth_edge(u, v, handler)

    def input_cars(self, car, handler):
        # input is a list [(x,y),(x,y)]
        self.cars += car 

        # draw cars
        G = self.map
        mapping = self.__mapping__(self.width, self.height)

        for x, y in self.cars:
            x_1, y_1 = mapping(x, y)
            handler.create_oval(x_1 - 10, y_1 - 10, x_1 + 10, y_1 + 10, fill='#0C69BF')


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

if __name__ == "__main__":
    point = (float(sys.argv[1]), float(sys.argv[2]))
    length = int(sys.argv[3])
    G = download_map(point, length)

    root = tk.Tk()
    road_map = RoadMap(G)
    #road_map.load_map(buffer)

    root.geometry('1500x1500')
    canvas = init_canvas(root, 1500, 1500)

    road_map.draw_map(canvas)

    road_map.input_jammed_node(333307.4094043318, 6581667.751225858, canvas)
    road_map.input_smooth_node(333349.74592687737, 6581566.582857542, canvas)
    road_map.input_cars([(333307.4094043318, 6581667.751225858),(333349.74592687737, 6581566.582857542)], canvas)


    print(road_map.rectangle_points)
    road_map.rotate(30, (500, 500)  )
    road_map.draw_square(canvas)

    root.mainloop()