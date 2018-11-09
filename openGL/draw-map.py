from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

window = 0                                              # glut window number
width, height = 500, 400                                # map size
x, y = 0, 0                                             # origin is (0, 0) 
path_x_num, path_y_num = 3, 2                           # numbers of paths
px_width, py_width = 40, 40                              # width of every path
car_length, car_width = 20,12   #car model size
car = [[0, 30, 150]]    # list of lists. [direction(verticle-0 / horizontal-1), centeral axis x, y]. 
car_point = [] # list of lists. [start x, start y, rec width, rec height]

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd() 


def path(x_map_base, y_map_base, x_num, y_num, width, height, px_width, py_width):
    # x_map_base & y_map_base is usually (0.0, 0.0)

    rectangle_point_1 = []      # starting x 
    rectangle_point_2 = []      # starting y
    rectangle_point_3 = []      # rec width
    rectangle_point_4 = []      # rec height

    # verticle direction path triangles
    for i in range(0, x_num):
        rectangle_point_1 = rectangle_point_1 + [x_map_base + 0.0 + i * (width - px_width + 0.0 - x_map_base) / (x_num - 1)]

    rectangle_point_2 = rectangle_point_2 + ([y_map_base] * x_num)
    rectangle_point_3 = rectangle_point_3 + ([px_width] * x_num)
    rectangle_point_4 = rectangle_point_4 + ([height - y_map_base * 2.0] * x_num)

    for i in range(0, y_num):
        rectangle_point_2 = rectangle_point_2 + [y_map_base + 0.0 + i * (height - py_width + 0.0 - y_map_base) / (y_num - 1)]

    rectangle_point_1 = rectangle_point_1 + ([x_map_base] * y_num)
    rectangle_point_3 = rectangle_point_3 + ([width - x_map_base * 2.0] * y_num)
    rectangle_point_4 = rectangle_point_4 + ([py_width] * y_num)
    
    return (rectangle_point_1, rectangle_point_2, rectangle_point_3, rectangle_point_4)


# the street images, if needed updated, can shift inside draw function
(point1, point2, point3, point4) = path(x, y, path_x_num, path_y_num, width, height, px_width, py_width)


def refresh2d(width, height):						# tell opengl we want to draw in 2D	
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def set_car_point():
    for i in range(len(car)):
        h = car[i][0]
        cx = car[i][1]
        cy = car[i][2]
        a = []
        a.append(cx - car_width * (1 - h) / 2.0 - car_length * h / 2.0)
        a.append(cy - car_width * h / 2.0 - car_length * (1 - h) / 2.0)
        a = a + [car_width * (1 - h) + car_length * h, car_width * h + car_length * (1 - h)]
        car_point.append(a)

def draw_car():
    set_car_point()
    glColor3f(0.2, 0.15, 0.0) 
    for i in range(len(car_point)):
        a = car_point[i]
        #draw_rect(a[0], a[1], a[2], a[3])
        draw_rect(*a)


def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
   
    refresh2d(width, height)                           # set mode to 2d

    # ToDo draw rectangle   
    glColor3f(0.4, 0.4, 0.4)                           # set color to blue
    draw_rect(0, 0, width, height)                      # rect  background
    #glutSwapBuffers()                                  # important for double buffering
   

    glColor3f(0.2,0.75,0.1)

    for i in range(len(point1)):
        draw_rect(point1[i], point2[i], point3[i], point4[i])
        #glutSwapBuffers()                                  # important for double buffering

    draw_car()

    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("test-triangle")             # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything