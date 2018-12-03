import numpy
import sys

#TBD: General interface
#TBD: Multi-car

class RiskZone(object):
    '''
    Basic: Given location and velocity, return edge of velocity
    '''
    def __init__(self, cal_func):
        self.func = cal_func
        self.zone = None

    def update(self, param):
        self.zone = self.func(param)
        return self.zone

def naive_func(param, dpkg_func):
    v, width, offset, mu = dpkg_func(param)
    zone = {'loc':offset, 'edge':[]}
    hight = (v**2)/(mu*9.8)

    tl = (offset[0] - 0.5*width), (offset[1] + hight)
    tr = (offset[0] + 0.5*width), (offset[1] + hight)
    bl = (offset[0] - 0.5*width), offset[1]
    br = (offset[0] + 0.5*width), offset[1]

    zone['edge'] = [tl, tr, bl, br]

    return zone


def dpkg(param):
    v = param['velocity']
    width = param['width']
    offset = param['loc']
    mu = param['mu']

    return v, width, offset, mu

#Usage

if __name__ == '__main__':
    v = float(sys.argv[1])/3.6
    loc = float(sys.argv[2]), float(sys.argv[3])
    param = {'velocity': v, 'loc': loc, 'width': 2, 'mu': 0.8}

    rz = RiskZone(lambda x: naive_func(x, dpkg))
    print(rz.update(param))
    
