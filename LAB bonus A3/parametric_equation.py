import time
from math import sin, cos, pi
from OpenGL.GL import *
from OpenGL.GLUT import *

# def drawPoint(x, y):
#     glPointSize(5) #pixel size. by default 1 thake
#     glBegin(GL_POINTS)
#     glVertex2f(x,y) #jekhane show korbe pixel
#     glEnd()

def draw_lines():
    glBegin(GL_LINES)
    glColor3f(2.0,0.0,3.0)
    glVertex2f(250, 50)
    glVertex2f(150,50)
    glVertex2f(350,400)
    glVertex2f(300,400)
    glEnd()

# def pe():
#     radius = 150
#     for angle in range (0,360,6):
#         theta = angle * pi/180
#         x = radius * cos(theta)
#         y = radius * sin(theta)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

d = 0

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    #call the draw methods here
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    draw_lines()
    glutSwapBuffers()

def animate():
    time.sleep(0.0005)
    # animation updates here
    global d
    d += 1
    if d > 500:
        d = 0

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name

glutDisplayFunc(showScreen)
glutIdleFunc(animate)

glutMainLoop()