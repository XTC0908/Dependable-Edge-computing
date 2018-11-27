from rdflib import Namespace
from rdflib import Graph
from rdflib import Literal, BNode
from rdflib.namespace import RDF, RDFS, XSD
import rdflib
import osmnx as nx


oslc  = Namespace('http://open-services.net/ns/core#')
sh    = Namespace('http://www.w3.org/ns/shacl')
pddl  = Namespace('http://ontology.cf.ericsson.net/pddl/')
pddle = Namespace('http://ontology.cf.ericsson.net/pddl_example/')

domain = Graph()
domain.bind(prefix = 'oslc', namespace = oslc)
domain.bind(prefix = 'sh', namespace = sh)
domain.bind(prefix = 'pddl', namespace = pddl)
domain.bind(prefix = 'pddle', namespace = pddle)

problem = Graph()


problem.parse('problem.ttl', format='turtle')
problem.parse('domain.ttl', format='turtle')

#for s, p, o in problem.triples((pddle.b, None, None)):
#    print(s, p, o)
pddle_problem = rdflib.term.URIRef('http://ontology.cf.ericsson.net/pddl_example/edge-computing-problem')
pddle_visible_x = rdflib.term.URIRef('http://ontology.cf.ericsson.net/pddl_example/visible-x')
pddle_visible_y = rdflib.term.URIRef('http://ontology.cf.ericsson.net/pddl_example/visible-y')

foo = BNode()
problem.add((pddle_problem, pddl.init, foo))
problem.add((foo, RDF.type, pddle.visible))
problem.add((foo, pddle_visible_x, pddle.f))
problem.add((foo, pddle_visible_y, pddle.e))


problem.add((pddle_problem, pddl.object, pddle.f))

problem.add((pddle.f, RDF.type, pddle.waypoint))
problem.add((pddle.f, oslc.instanceShape, pddl.ObjectShape))
problem.add((pddle.f, RDFS.label, Literal('f')))
with open('test_out.ttl', 'w') as out_file:
    text = domain.serialize(format='turtle').decode('utf-8')
    out_file.write(text)
    text = problem.serialize(format='turtle').decode('utf-8')
    out_file.write(text)

full_map = nx.load_graphml('./demo.graphml')

def problem_generator(full_map, start_points, end_points, template): 
    '''
    Start point: a tuple (u, v) of edge (road) where the vehicle is on
    End point: a tuple (u, v) of edge (road) where the vehicle finally stop
    Template: a template of rdf/turtle file
    '''
    
    problem = Graph()

    problem.bind(prefix = 'oslc', namespace = Namespace('http://open-services.net/ns/core#'))
    problem.bind(prefix = 'sh', namespace = sh)
    problem.bind(prefix = 'pddl', namespace = pddl)
    problem.bind(prefix = 'pddle', namespace = Namespace('http://ontology.cf.ericsson.net/pddl_example/'))

    problem.parse(template, format='turtle')
    
    #edge_list = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    #generate map
    for u, v in full_map.edges(keys=False, data=False):
        problem.add((pddle['edge-computing-problem'], pddl.object, pddle['way_point_'+str(u)]))
        problem.add((pddle['edge-computing-problem'], pddl.object, pddle['way_point_'+str(v)]))

        foo = BNode()
        problem.add((pddle['edge-computing-problem'], pddl.init, foo))
        problem.add((foo, RDF.type, pddle.visible))
        problem.add((foo, pddle['visible-x'], pddle['way_point_'+str(u)]))
        problem.add((foo, pddle['visible-y'], pddle['way_point_'+str(v)]))

        foo = BNode()
        problem.add((pddle['edge-computing-problem'], pddl.init, foo))
        problem.add((foo, RDF.type, pddle.visible))
        problem.add((foo, pddle['visible-x'], pddle['way_point_'+str(v)]))
        problem.add((foo, pddle['visible-y'], pddle['way_point_'+str(u)]))

        problem.add((pddle['way_point_'+str(u)], RDF.type, pddle.waypoint))
        problem.add((pddle['way_point_'+str(u)], oslc.instanceShape, pddl.ObjectShape))
        problem.add((pddle['way_point_'+str(u)], RDFS.label, Literal('way_point_'+str(u))))

        problem.add((pddle['way_point_'+str(v)], RDF.type, pddle.waypoint))
        problem.add((pddle['way_point_'+str(v)], oslc.instanceShape, pddl.ObjectShape))
        problem.add((pddle['way_point_'+str(v)], RDFS.label, Literal('way_point_'+str(v))))

    #generate start point, vehicle, pre-condition
    problem.add((pddle['edge-computing-problem'], pddl.object, pddle.way_point_start))
    problem.add((pddle['edge-computing-problem'], pddl.object, pddle.v))
    problem.add((pddle['edge-computing-problem'], pddl.object, pddle.dest))
    
    foo = BNode()
    problem.add((pddle['edge-computing-problem'], pddl.init, foo))
    problem.add((foo, RDF.type, pddle.visible))
    problem.add((foo, pddle['visible-x'], pddle['way_point_start']))
    problem.add((foo, pddle['visible-y'], pddle['way_point_'+str(start_points[0])]))

    foo = BNode()
    problem.add((pddle['edge-computing-problem'], pddl.init, foo))
    problem.add((foo, RDF.type, pddle.visible))
    problem.add((foo, pddle['visible-x'], pddle['way_point_start']))
    problem.add((foo, pddle['visible-y'], pddle['way_point_'+str(start_points[1])]))

    foo = BNode()
    problem.add((pddle['edge-computing-problem'], pddl.init, foo))
    problem.add((foo, RDF.type, pddle.on))
    problem.add((foo, pddle['on-x'], pddle['v']))
    problem.add((foo, pddle['on-y'], pddle['way_point_start']))

    problem.add((pddle['way_point_start'], RDF.type, pddle.waypoint))
    problem.add((pddle['way_point_start'], oslc.instanceShape, pddl.ObjectShape))
    problem.add((pddle['way_point_start'], RDFS.label, Literal('way_point_start')))

    problem.add((pddle['v'], RDF.type, pddle.vehicle))
    problem.add((pddle['v'], oslc.instanceShape, pddl.ObjectShape))
    problem.add((pddle['v'], RDFS.label, Literal('v')))

    #generate end point, vehicle, post-condition
    
    foo = BNode()
    problem.add((pddle['edge-computing-problem'], pddl.init, foo))
    problem.add((foo, RDF.type, pddle.visible))
    problem.add((foo, pddle['visible-y'], pddle.dest))
    problem.add((foo, pddle['visible-x'], pddle['way_point_'+str(end_points[0])]))

    foo = BNode()
    problem.add((pddle['edge-computing-problem'], pddl.init, foo))
    problem.add((foo, RDF.type, pddle.visible))
    problem.add((foo, pddle['visible-y'], pddle.dest))
    problem.add((foo, pddle['visible-x'], pddle['way_point_'+str(end_points[1])]))

    foo = BNode()
    bar = BNode()
    problem.add((pddle['edge-computing-problem'], pddl.goal, foo))
    problem.add((foo, RDF.type, pddl.And))
    problem.add((foo, pddl.argument, bar))
    problem.add((bar, RDF.type, pddle.on))
    problem.add((bar, pddle['on-x'], pddle.v))
    problem.add((bar, pddle['on-y'], pddle.dest))
    
    return problem

    
    
    
    #print(list(full_map.edges(keys=False, data=False)))

if __name__ == '__main__':
    full_map = nx.load_graphml('./demo.graphml')
    problem = problem_generator(full_map, (169822, 1755176087), (1393926005, 172605),'problem _template.ttl')

    domain = Graph()
    domain.parse('domain.ttl', format='turtle')

    with open('test_out.ttl', 'w') as wfile:
        wfile.write(domain.serialize(format="turtle").decode('utf-8'))
        wfile.write(problem.serialize(format="turtle").decode('utf-8'))