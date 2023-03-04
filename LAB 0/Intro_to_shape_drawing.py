from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(8) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)#jekhane show korbe pixel
    glEnd()
def draw_lines():
    glBegin(GL_LINES)
    glColor3f(2.0,0.0,3.0)
    glVertex2f(250, 50)
    glVertex2f(150,50)
    glVertex2f(350,400)
    glVertex2f(300,400)
    glEnd()

def draw_triangles():
    glBegin(GL_TRIANGLES)
    glColor3f(158.0/255,204.0/255,4.0/255)
    glVertex2f(100,200)
    glVertex2f(150, 250)
    glVertex2f(300, 200)
    glEnd()

def draw_quads():
    glBegin(GL_QUADS)
    glColor3f(1.0,4.0,0.0)
    glVertex2f(200, 250)
    glVertex2f(300, 250)
    glVertex2f(300, 350)
    glVertex2f(200, 350)
    glEnd()
def draw_polygon():
    glBegin(GL_POLYGON)
    glVertex(100,100)
    glVertex(80, 50)
    glVertex(100, 150)
    glVertex(180, 150)
    glVertex(200, 50)
    glVertex(180, 100)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 5.0, 3.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(120, 40)
    draw_points(210, 140)
    draw_triangles()
    draw_lines()
    draw_quads()
    draw_polygon()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(650, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Practice of drawing shapes") #window name
glutDisplayFunc(showScreen)

glutMainLoop()