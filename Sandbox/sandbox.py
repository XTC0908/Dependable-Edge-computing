import numpy as np
import osmnx as ox
import utm
import rdflib
from rdflib.namespace import RDF, RDFS, XSD
from rdflib import Namespace
from rdflib import Literal, BNode, URIRef
import numpy as np
import time
from calc_riskzone import risk_zone, overlapping
from interfaceToViz import InterfaceViz
import time
import sys
from Server import *

sys.path.append('../rdf_generator/')
sys.path.append('../interface/')

from problemGenerator import Generator
from interface import InterfacePlanner

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
        self.planner = InterfacePlanner()
        self.problem_generator = None
        
    def __init_RDF__(self):
        G = rdflib.Graph()
        G.bind('edge', edge)
        G.bind('entity', entity)
        return G

    def add_vehicle(self, vehicle):
        G = self.top
        step_rdf = rdflib.Graph()
        v = BNode()
        G.add((edge.sandbox, entity.vehicle, v))
        G.add((v, entity.vid, Literal(vehicle['vid'])))
        
        pos = list(vehicle['position'])
        dest = list(vehicle['dest'])

        G.add((v, entity.pos, Literal(pos)))
        G.add((v, entity.time_stamp, Literal(vehicle['time_stamp'])))
        G.add((v, entity.velocity, Literal(0)))
        G.add((v, entity.dest, Literal(dest)))
        G.add((v, entity.plan, Literal(None)))
        G.add((v, entity.risk, Literal(None)))

        on = self.on_query(pos)
        G.add((v, entity.on, Literal(on)))

        to = self.on_query(dest)
        G.add((v, entity.to, Literal(to)))

        utm_pos = toUtm(vehicle['position'])
        utm_dst = toUtm(vehicle['dest'])


        problem = self.problem_generator(on, to)

        try:
            with open('./tmp.ttl', 'w') as tmp:
                r = self.planner.generate_plan('http://localhost:3021', problem.serialize(format='turtle'))
                tmp.write(r.text)
            step = self.__step_parse(step_rdf.parse('./tmp.ttl', format='turtle'))
            step = sorted(step, key=lambda x: x[0])
        except:
            print("rdf_error")

        self.viz.car_req({'id':vehicle['vid'], 'x': utm_pos[0], 'y': utm_pos[1]})
        G.add((v, entity.plan, Literal(step)))

        return step
        #self.viz.car_req({'id':123, 'x': utm_dst[0], 'y': utm_dst[1]})
        
        #for road in step:
        #    if road[3] != None:
        #        ux, uy = road[3]
        #        vx, vy = road[4]
#
        # 


    def __step_parse(self, step_rdf):
        step_list = []
        for step, order in step_rdf.subject_objects(predicate=URIRef('http://www.w3.org/ns/shacl#order')):
            x = step_rdf.value(subject=step, predicate=pddl.action)
            start = step_rdf.value(subject=BNode(x), predicate=pddle['move-x'])[55:]
            end = step_rdf.value(subject=BNode(x), predicate=pddle['move-y'])[55:]
            if len(end)==0:
                end = 'dest'
            try:
                u = int(start)
                v = int(end)
                p_start = list(self.top.subjects(predicate=entity.pid, object=Literal(u)))[0]
                p_end = list(self.top.subjects(predicate=entity.pid, object=Literal(v)))[0]
                p_start = self.top.value(subject=p_start, predicate=entity.pos).value
                p_end = self.top.value(subject=p_end, predicate=entity.pos).value
            except:
                p_start=None
                p_end = None
                #print('???')
            step_list.append((order.value, start, end, p_start, p_end))
        return step_list


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
    
        print('update:', vehicle)
        risk = risk_zone(velocity, pos)
        G.set((BNode(v), entity.risk, Literal(risk)))
        G.set((BNode(v), entity.time_stamp, Literal(t)))
        G.set((BNode(v), entity.pos, Literal(vehicle['position'])))
        G.set((BNode(v), entity.on, Literal(self.on_query(vehicle['position']))))
        
        self.viz.car_req({'id':vehicle['vid'], 'x': pos[0], 'y': pos[1]})
        flag = False
        for s, p, o in G.triples((None, entity.risk, None)):
            z = o.value
            vid_t = G.value(BNode(s), entity.vid)
            if vid_t != vehicle['vid']:
                flag = flag or overlapping(z, risk)
                if flag:
                    self.viz.risk_zone_req({'id':vehicle['vid'], 'x': pos[0], 'y': pos[1],  \
                                            'dot1':tuple(risk[0]), 'dot2':tuple(risk[1]),   \
                                            'dot3':tuple(risk[2]), 'dot4':tuple(risk[3]),    \
                                            'color':"red"})
                    
                    self.viz.risk_zone_req({'id':vehicle['vid'], 'x': pos[0], 'y': pos[1], \
                                            'dot1':tuple(z[0]), 'dot2':tuple(z[1]),        \
                                            'dot3':tuple(z[2]), 'dot4':tuple(z[3]),       \
                                            'color':"red"})
        if not flag:
            self.viz.risk_zone_req({'id':vehicle['vid'], 'x': pos[0], 'y': pos[1],  \
                                        'dot1':tuple(risk[0]), 'dot2':tuple(risk[1]),   \
                                        'dot3':tuple(risk[2]), 'dot4':tuple(risk[3]),    \
                                        'color':"#162C22"})


        jam = vehicle['sensor']
        print(jam)
        if jam == 'jam':
            u = int(vehicle['u'])
            v = int(vehicle['v'])
            print('hear')
            self.viz.road_req({'id':123, 'ux':u, 'uy':0, 'vx':v, 'vy':0, 'state':'jam'})
            if self.map.has_edge(u, v):
                print('got u v')
                self.map.remove_edge(u, v)
            if self.map.has_edge(v, u):
                print('got v u')
                self.map.remove_edge(v, u)
            print(u, v)
            self.problem_generator = lambda s, e: Generator(self.map, s, e)
            print('s', self.problem_generator)

    def load_map(self, map_path, folder):
        G = self.top
        map_G = ox.load_graphml(map_path, folder=folder)

        self.map = map_G
        self.problem_generator = lambda s, e: Generator(map_G, s, e)
        print(self.problem_generator)

        map_info = BNode()
        G.add((edge.sandbox, entity.map, map_info))

        for u, v in map_G.edges(keys=False, data=False):
            path = BNode()
            G.add((map_info, entity.path, path))
            
            waypoint = BNode()
            G.add((path, entity.waypoint, waypoint))
            G.add((waypoint, entity.pid, Literal(u)))
            G.add((waypoint, entity.pos, Literal([float(map_G.nodes[u]['lat']), float(map_G.nodes[u]['lon'])])))

            waypoint = BNode()
            G.add((path, entity.waypoint, waypoint))
            G.add((waypoint, entity.pid, Literal(v)))
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
                return [G.value(subject=wps[0], predicate=entity.pid).value, G.value(subject=wps[1], predicate=entity.pid).value]
            elif np.sum((pos - pos0)**2) > np.sum((pos1 - pos0)**2):
                pass
            else:
                k = (pos1[0] - pos0[0]) / (pos1[1] - pos0[1])
                k2 = (pos[0] - pos0[0]) / (pos[1] - pos0[1])
                if (k-k2) <= 1e-5 and (k2-k) <= 1e-5:
                    return [G.value(subject=wps[0], predicate=entity.pid).value, G.value(subject=wps[1], predicate=entity.pid).value]
        return None

if __name__ == '__main__':
    sandbox = Sandbox()
    sandbox.load_map('demo.graphml', '../Viz/data/')
    handler = ConstructHandler(sandbox)
    start_server(('', 9000), handler)
    #sandbox.load_map('demo.graphml', '../Viz/data/')
    #sandbox.add_vehicle({'vid':1, 'position':(59.3365935,18.0674845), 'dest':(59.3428782,18.078231), 'time_stamp': 0.000})
        
        