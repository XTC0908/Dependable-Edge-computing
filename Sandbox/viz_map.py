import tkinter as tk
import osmnx as ox
import sys
from util import download_map

class RoadMap(object):
    def __init__(self, road_map=None):
        self.map = road_map
        if road_map != None:
            edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
            self.bbox = edges.total_bounds #west, south, east, north
        else:
             self.bbox = None
        
    
    def load_map(self, path):
        self.map = ox.load_graphml(path)
        edges = ox.graph_to_gdfs(self.map, nodes=False, fill_edge_geometry=True)
        self.bbox = edges.total_bounds #west, south, east, north

    def draw_map(self, handler):
        handler.delete('all')
        width, height = handler.winfo_width(), handler.winfo_height()
        G = self.map
        mapping = self.__mapping__(width, height)

        for u, v in G.edges(keys=False, data=False):
            x_1, y_1 = mapping(G.nodes[u]['x'], G.nodes[u]['y'])
            x_2, y_2 = mapping(G.nodes[v]['x'], G.nodes[v]['y'])
            handler.create_line(x_1, y_1, x_2, y_2, width=5, fill='#B0B0B0')


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

    root.mainloop()