import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action='error', category=RuntimeWarning)

def bbox(v, size, offset = np.zeros(2)):
    '''
    v: vector2d, (Vx, Vy)
    size: tuple, (width, length)
    return:
        point: (x1, x2, x3, x4)
    '''
    try:
        norm = lambda x: x/np.sqrt(np.sum(x**2))
        v1 = np.array([1, -(v[0]/v[1])])
        v2 = np.array([-1, (v[0]/v[1])])

        v1 = (0.5*size[0])*norm(v1)
        v2 = (0.5*size[0])*norm(v2)

        v3 = (0.5*size[1])*norm(v)
    except:
        return [offset, offset, offset, offset]

    return [v1+offset, v1+v3+offset, v2+v3+offset, v2+offset]

def overlapping(bbox1, bbox2):
    '''
    bbox1: list (vertex1, vertex2, vertex3, vertex4)
    bbox2: list (vertex1, vertex2, vertex3, vertex4)
    '''
    flag = False
    for v1 in bbox1:
        flag = flag or point_in_rect(v1, bbox2)

    for v2 in bbox2:
        flag = flag or point_in_rect(v2, bbox1)

    return flag

def point_in_rect(p, bbox):
    a_edge = np.array([np.array((bbox[(i-1)%4][1]-bbox[i][1], bbox[i][0]-bbox[(i-1)%4][0])) for i in range(4)])
    sig = np.einsum('ij, ij->i', (p - np.array(bbox)), a_edge)

    return (sig > 0).all() 


def cal_size(V_vec, mu=0.8, width=2):
    v = (np.sum(V_vec**2))
    hight = (v)/(mu*9.8)
    return (width, hight)

def risk_zone(V_vec, loc):
    size = cal_size(V_vec)
    return bbox(V_vec, size, np.array(loc))

if __name__=='__main__':
    draw_vector = lambda x: plt.plot([0, x[0]], [0, x[1]])
    draw_line = lambda x, y: plt.plot([y[0], x[0]], [y[1], x[1]])
    
    v1 = np.array([12, 3])
    size1 = cal_size(v1)

    v2 = np.array([-12, 10])
    size2 = cal_size(v2)

    v1_list = bbox(v1, size1, np.array((0, 0)))
    v2_list = bbox(v2, size2, np.array((6, -4)))

    #print(v1_list, v2_list)
    
    for i, vtx in enumerate(v1_list):
        draw_line(vtx, v1_list[(i-1)%4])

    for i, vtx in enumerate(v2_list):
        draw_line(vtx, v2_list[(i-1)%4])
    
    print(overlapping(v1_list, v2_list))
    plt.show()




