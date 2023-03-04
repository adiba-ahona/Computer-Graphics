from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

x = random.sample(range(0,600),50)
y = random.sample(range(0,600),50)

def draw_pixel():
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(50):
        glVertex2f(x[i], y[i])#jekhane show korbe pixel
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
    glColor3f(1.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_pixel()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"19101257_Drawing pixel") #window name
glutDisplayFunc(showScreen)

glutMainLoop()