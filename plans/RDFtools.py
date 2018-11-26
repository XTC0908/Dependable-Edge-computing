import rdflib

G = rdflib.Graph()
G.parse('./domain.ttl', format='turtle')
print(G)