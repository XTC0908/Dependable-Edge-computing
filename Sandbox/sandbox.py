import numpy as np
import osmnx as ox
import utm
import rdflib
#from interface import general_http_interface
#from interface import interface
#from rdf_generator import problemGenerator
from rdflib.namespace import RDF, RDFS, XSD
from rdflib import Namespace
from rdflib import Literal, BNode
import numpy as np
import time
from calc_riskzone import risk_zone, overlapping
from interfaceToViz import InterfaceViz
import time

oslc  = Namespace('http://open-services.net/ns/core#')
sh    = Namespace('http://www.w3.org/ns/shacl')
edge  = Namespace('http://dependable-edge.gru/edge#')
entity  = Namespace('http://dependable-edge-entity.gru/entity#')
pddl  = Namespace('http://ontology.cf.ericsson.net/pddl/')
pddle = Namespace('http://ontology.cf.ericsson.net/pddl_example/')

toUtm = lambda x: np.array(utm.from_latlon(x[0], x[1])[:2])

class Sandbox(object):
    def __init__(self):
        self.top = self.__init_RDF__()
        self.viz = InterfaceViz('http://localhost:8888')
        
    def __init_RDF__(self):
        G = rdflib.Graph()
        G.bind('edge', edge)
        G.bind('entity', entity)
        return G

    def add_vehicle(self, vehicle):
        
        G = self.top
        v = BNode()
        G.add((edge.sandbox, entity.vehicle, v))
        G.add((v, entity.vid, Literal(vehicle['vid'])))
        
        pos = list(vehicle['position'])

        G.add((v, entity.pos, Literal(pos)))
        G.add((v, entity.time_stamp, Literal(vehicle['time_stamp'])))
        G.add((v, entity.velocity, Literal(0)))
        G.add((v, entity.dest, Literal(None)))
        G.add((v, entity.plan, Literal(None)))
        G.add((v, entity.risk, Literal(None)))

        on = self.on_query(pos)
        G.add((v, entity.on, Literal(on)))
        
        utm_pos = toUtm(vehicle['position'])
        self.viz.car_req({'id':vehicle['vid'], 'x': utm_pos[0], 'y': utm_pos[1]})


    def update_vehicle(self, vehicle):
        G = self.top
        t = vehicle['time_stamp']
        pos = toUtm(vehicle['position'])
        vid = vehicle['vid']

        v = G.value(object = Literal(vid), predicate=entity.vid)
        dt = t - (G.value(subject = BNode(v), predicate=entity.time_stamp).value)
        dpos = pos - toUtm(G.value(subject = BNode(v), predicate=entity.pos).value)
        try:
            velocity = (dpos/dt)
            G.set((BNode(v),entity.velocity, Literal(velocity)))
        except ZeroDivisionError:
            pass
        
        risk = risk_zone(velocity, pos)
        G.set((BNode(v), entity.risk, Literal(risk)))
        G.set((BNode(v), entity.time_stamp, Literal(t)))
        G.set((BNode(v), entity.pos, Literal(vehicle['position'])))
        G.set((BNode(v), entity.on, Literal(self.on_query(vehicle['position']))))
        
        #self.viz.car_req({'id':vehicle['vid'], 'x': pos[0], 'y': pos[1]})
        #time.sleep(0.5)
        self.viz.risk_zone_req({'id':vehicle['vid'], 'x': pos[0], 'y': pos[1], \
                                'dot1':tuple(risk[0]), 'dot2':tuple(risk[1]), \
                                'dot3':tuple(risk[2]), 'dot4':tuple(risk[3])})

    def load_map(self, map_path, folder):
        G = self.top
        map_G = ox.load_graphml(map_path, folder=folder)

        self.map = map_G
        
        map_info = BNode()
        G.add((edge.sandbox, entity.map, map_info))

        for u, v in map_G.edges(keys=False, data=False):
            path = BNode()
            G.add((map_info, entity.path, path))
            
            waypoint = BNode()
            G.add((path, entity.waypoint, waypoint))
            G.add((waypoint, entity.vid, Literal(u)))
            G.add((waypoint, entity.pos, Literal([float(map_G.nodes[u]['lat']), float(map_G.nodes[u]['lon'])])))

            waypoint = BNode()
            G.add((path, entity.waypoint, waypoint))
            G.add((waypoint, entity.vid, Literal(v)))
            G.add((waypoint, entity.pos, Literal([float(map_G.nodes[v]['lat']), float(map_G.nodes[v]['lon'])])))

    def on_query(self, pos):
        G = self.top
        pos = np.array(pos)
        for path in G.objects(predicate = entity.path):
            wps = list(G.objects(subject=path, predicate=entity.waypoint))
            pos0 = np.array(G.value(subject=wps[0], predicate=entity.pos).value)
            pos1 = np.array(G.value(subject=wps[1], predicate=entity.pos).value)
            #print(np.abs(pos - pos1), np.abs(pos - pos0))
            if np.abs(pos - pos0).all() < 1e-6 or np.abs(pos - pos1).all() < 1e-6:
                return [G.value(subject=wps[0], predicate=entity.vid).value, G.value(subject=wps[1], predicate=entity.vid).value]
            elif np.sum((pos - pos0)**2) > np.sum((pos1 - pos0)**2):
                pass
            else:
                k = (pos1[0] - pos0[0]) / (pos1[1] - pos0[1])
                k2 = (pos[0] - pos0[0]) / (pos[1] - pos0[1])
                if (k-k2) <= 1e-5 and (k2-k) <= 1e-5:
                    return [G.value(subject=wps[0], predicate=entity.vid).value, G.value(subject=wps[1], predicate=entity.vid).value]
        return None

if __name__ == '__main__':
    sandbox = Sandbox()
    sandbox.load_map('demo.graphml', '../Viz/data/')
    sandbox.add_vehicle({'vid':1, 'position':(59.3365935,18.0674845), 'time_stamp': 0.000})
    time.sleep(2)
    sandbox.update_vehicle({'vid':1, 'position':(59.3366178505,18.067988932), 'time_stamp':1.00})
    time.sleep(2)
    sandbox.update_vehicle({'vid':1, 'position':(59.33665634,18.06878626), 'time_stamp': 2.00})
    #sandbox.update_vehicle({'vid':1, 'position':(59.3365936571,18.0674877544), 'time_stamp': 0.003})
    #sandbox.update_vehicle({'vid':1, 'position':(59.3365936571,18.0674877544), 'time_stamp': 0.004})
    #sandbox.update_vehicle({'vid':1, 'position':(59.3365936571,18.0674877544), 'time_stamp': 0.500})
#
    #sandbox.add_vehicle({'vid':1, 'position':(59.3366635666,18.0689359624), 'time_stamp': 0.000})
    #sandbox.add_vehicle({'vid':1, 'position':(59.3367506,18.0707389), 'time_stamp': 0.000})
    #sandbox.on_query((0, 0))
    
    #print(sandbox.top.serialize(format='turtle').decode('utf-8'))
    #hello = sandbox.top.value(Literal('Sandbox'), edge.hello)
        
        