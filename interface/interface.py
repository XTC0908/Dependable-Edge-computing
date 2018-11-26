import requests
import json

class InterfacePlanner(object):
    def __init__(self):
        self.generate_pddl_header = {'Accept':'text/x-pddl',
                                     'Content-Type':'application/turtle'}
        self.generate_plan_header = {'Accept':'application/turtle', 
                                     'Content-Type':'application/turtle'}

        self.generate_plan_url = '/planner/planCreationFactory'
        self.generate_pddl_url = '/planner/pddlCreationFactory'
        self.generate_validated_url = '/planner/validatedPlanCreationFactory'

    def generate_pddl(self, url, ttl):
        with open(ttl, 'r') as f:
            data = f.read()
            r = requests.post((url + self.generate_pddl_url), data=data, headers = self.generate_pddl_header)
            return r


    def generate_plan(self, url, ttl):
        with open(ttl, 'r') as f:
            data = f.read()
            r = requests.post((url + self.generate_plan_url), data=data, headers = self.generate_pddl_header)
            return r

    def generate_validated_plan(self, url, ttl):
        with open(ttl, 'r') as f:
            data = f.read()
            r = requests.post((url + self.generate_validated_url), data=data, headers = self.generate_plan_header)
            return r


if __name__=='__main__':
    planner = InterfacePlanner()
    r = planner.generate_validated_plan('http://localhost:3021', './domain_feasible.ttl')
    print(r.text)