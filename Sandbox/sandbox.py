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

oslc  = Namespace('http://open-services.net/ns/core#')
sh    = Namespace('http://www.w3.org/ns/shacl')
edge  = Namespace('http://dependable-edge.gru/edge#')
entity  = Namespace('http://dependable-edge-entity.gru/entity#')
pddl  = Namespace('http://ontology.cf.ericsson.net/pddl/')
pddle = Namespace('http://ontology.cf.ericsson.net/pddl_example/')

class Sandbox(object):
    def __init__(self):
        self.top = self.__init_RDF__()
        
    def __init_RDF__(self):
        G = rdflib.Graph()
        return G

    def add_vehicle(self, vehicle):
        latlon2utm = lambda x: utm.from_latlon(x[0], x[1])
        
        G = self.top
        v = BNode()
        G.add((edge.sandbox, entity.vehicle, v))
        G.add((v, entity.id, Literal(vehicle['id'])))
        
        pos = list(latlon2utm(vehicle['position'])[:2])
        G.add((v, entity.pos, Literal(pos)))

        G.add((v, entity.time_stamp, Literal(vehicle['time_stamp'])))

        G.add((v, entity.velocity, Literal(vehicle['velocity'])))

        on = self.on_query(pos)
        G.add((v, entity.on, Literal(on)))

        print(on)
        print(self.map.nodes[on[0]])
        print(self.map.nodes[on[1]])


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
            G.add((waypoint, entity.id, Literal(u)))
            G.add((waypoint, entity.pos, Literal([map_G.nodes[u]['x'], map_G.nodes[u]['y']])))

            waypoint = BNode()
            G.add((path, entity.waypoint, waypoint))
            G.add((waypoint, entity.id, Literal(v)))
            G.add((waypoint, entity.pos, Literal([map_G.nodes[v]['x'], map_G.nodes[v]['y']])))

    def on_query(self, pos):
        G = self.top
        pos = np.array(pos)
        print(pos)
        for path in G.objects(predicate = entity.path):
            wps = list(G.objects(subject=path, predicate=entity.waypoint))
            pos0 = np.array(G.value(subject=wps[0], predicate=entity.pos).value)
            pos1 = np.array(G.value(subject=wps[1], predicate=entity.pos).value)
            if (pos - pos0).all() < 1e-5 or (pos - pos0).all() < 1e-5:
                return [G.value(subject=wps[0], predicate=entity.id).value, G.value(subject=wps[1], predicate=entity.id).value]
            elif np.sum((pos - pos0)**2) > np.sum((pos1 - pos0)**2):
                pass
            else:
                k = (pos0[0] - pos0[1]) / (pos1[0] - pos1[1])
                k2 = (pos[1] - pos0[1]) / (pos[1] - pos1[1])
                if (k-k2) <= 1e-5:
                    return [G.value(subject=wps[0], predicate=entity.id).value, G.value(subject=wps[1], predicate=entity.id).value]

        return None

if __name__ == '__main__':
    sandbox = Sandbox()
    sandbox.load_map('demo.graphml', '../Viz/data/')
    sandbox.add_vehicle({'id':1, 'position':(59.3365935,18.0674845), 'time_stamp': 0.000, 'velocity': 0.0000})
    #sandbox.on_query((0, 0))
    
    #print(sandbox.top.serialize(format='turtle').decode('utf-8'))
    #hello = sandbox.top.value(Literal('Sandbox'), edge.hello)
        
        