import numpy as np
import osmnx as ox
from viz_map import RoadMap

class Vehicle(object):
    def __init__(self):
        pass
    
class FleetManagement(object):
    def __init__(self):
        pass

class Sandbox(object):
    def __init__(self):
        self.__map__ = None
        self.__vehicle__ = {}

    def add_vehicle(self, vehicle):
        vid = hash(vehicle)
        self.__vehicle__[vid] = vehicle

        return vid

    def add_vehicle(self, vid):
        return self.__vehicle__.pop(vid)

    def update_vehicle(self, vid, segment, value):
        return self.__vehicle__[vid].update(segment, value)

    def 
        
        