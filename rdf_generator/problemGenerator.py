from rdflib import Namespace
from rdflib import Graph
from rdflib import Literal, BNode
from rdflib.namespace import RDF, RDFS, XSD
import rdflib
import osmnx as nx


oslc  = Namespace('http://open-services.net/ns/core')
sh    = Namespace('http://www.w3.org/ns/shacl')
pddl  = Namespace('http://ontology.cf.ericsson.net/pddl/')
pddle = Namespace('http://ontology.cf.ericsson.net/pddl_example/')

domain = Graph()
domain.bind(prefix = 'oslc', namespace = oslc)
domain.bind(prefix = 'sh', namespace = sh)
domain.bind(prefix = 'pddl', namespace = pddl)
domain.bind(prefix = 'pddle', namespace = pddle)

problem = Graph()
problem.bind(prefix = 'oslc', namespace = oslc)
problem.bind(prefix = 'sh', namespace = sh)
problem.bind(prefix = 'pddl', namespace = pddl)
problem.bind(prefix = 'pddle', namespace = pddle)

problem.parse('problem.ttl', format='turtle')

for s, p, o in problem.triples((pddle.b, None, None)):
    print(s, p, o)
pddle_problem = rdflib.term.URIRef('http://ontology.cf.ericsson.net/pddl_example/edge-computing-problem')
pddle_visiable_x = rdflib.term.URIRef('http://ontology.cf.ericsson.net/pddl_example/visible-x')
pddle_visiable_y = rdflib.term.URIRef('http://ontology.cf.ericsson.net/pddl_example/visible-y')

foo = BNode()
problem.add((pddle_problem, pddl.init, foo))
problem.add((foo, RDF.type, pddle.visible))
problem.add((foo, pddle_visiable_x, pddle.f))
problem.add((foo, pddle_visiable_y, pddle.e))

bar = BNode()
problem.add((pddle.f, RDF.type, pddle.waypoint))
problem.add((pddle.f, oslc.instanceShape, pddl.ObjectShape))
problem.add((pddle.f, RDFS.label, Literal('f')))
with open('test_out.ttl', 'w') as out_file:
    text = problem.serialize(format='turtle').decode('utf-8')
    out_file.write(text)

full_map = nx.load_graphml('./demo.graphml')

#for u, v in full_map.edges(keys=False, data=False):
