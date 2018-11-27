class RoadMap(object):

    jam_edge = []
    smooth_edge = []
    cars = [{"id": 1, "x": 333307.4094043318, "y": 6581667.751225858},\
        {"id": 2, "x": 333307, "y": 6581560}]
    safetyzone = []



    def __init__(self, road_map=None):
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

    def input_smooth_node(self, smooth_node_x, smooth_node_y, handler):
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
        if car_dic_element['category'] is not 'car':
            return 
        ID, x, y = car_dic_element['id'], car_dic_element['x'], car_dic_element['y']
        newcar = {'id': ID, 'x': x, 'y': y}
        for c in self.cars:
            if c['id'] == ID:
                self.cars.remove(c)
                break
        self.cars.append(newcar)    

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