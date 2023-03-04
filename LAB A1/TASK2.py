from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_lines():
    glLineWidth(4)
    glEnable(GL_LINE_SMOOTH)
    glBegin(GL_LINES)

    # triangle/roof
    glColor3f(81.0/255, 8.0/255, 16.0/255)
    glVertex2f(200, 500)
    glVertex2f(100, 400)
    glVertex2f(300, 400)
    glVertex2f(200, 500)

    # House body
    glColor3f(245.0/255, 83.0/255, 181.0/255)
    glVertex2f(100, 400)
    glVertex2f(100, 200)

    glVertex2f(100, 200)
    glVertex2f(300, 200)

    glVertex2f(300, 200)
    glVertex2f(300, 400)

    glVertex2f(300, 400)
    glVertex2f(100, 400)

    # window1
    glColor3f(66.0/255, 248.0/255, 240.0/255)
    glVertex2f(120, 370)
    glVertex2f(120, 330)
    glVertex2f(120, 330)
    glVertex2f(160, 330)
    glVertex2f(160, 330)
    glVertex2f(160, 370)
    glVertex2f(160, 370)
    glVertex2f(120, 370)

    # window2
    glVertex2f(240, 370)
    glVertex2f(240, 330)
    glVertex2f(240, 330)
    glVertex2f(280, 330)
    glVertex2f(280, 330)
    glVertex2f(280, 370)
    glVertex2f(280, 370)
    glVertex2f(240, 370)

    #door
    glColor3f(255.0/255, 253.0/255, 83.0/255)
    glVertex2f(170, 200)
    glVertex2f(170, 300)
    glVertex2f(170, 300)
    glVertex2f(230, 300)
    glVertex2f(230, 300)
    glVertex2f(230, 200)
    glVertex2f(230, 200)
    glVertex2f(170, 200)
    glEnd()

    #doorknob
    glPointSize(7)
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glColor3f(238.0/255, 149.0/255, 61.0/255)
    glVertex2f(220.0, 250.0)
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
    draw_lines()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 570) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2: A House") #window name
glutDisplayFunc(showScreen)

glutMainLoop()