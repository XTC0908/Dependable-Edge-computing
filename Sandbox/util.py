import sys
import osmnx as ox


def download_map(location_point, range):
    G = ox.graph_from_point(location_point, distance=range, simplify=False, network_type='drive')
    G = ox.project_graph(G)
    return G