from OpenGL.GL import *
from OpenGL.GLUT import *

def midPoint(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    E = 2 * dy
    NE = 2 * (dy - dx)
    x = x0
    y = y0
    while x < x1:
        if d <= 0:
            d += E
            x += 1

        else:
            d += NE
            x += 1
            y += 1

        drawPoint(x, y)

def DDA(x1, y1, x2, y2):
    m = (y2 - y1)/(x2 - x1)
    if -1 < m < 1:
        glBegin(GL_POINTS)
        while x1 < x2:
            x1 += 1
            y1 += m
            glVertex2f(x1, round(y1))
        glEnd()
    else:
        glBegin(GL_POINTS)
        while y1 < y2:
            x1 += 1/m
            y1 += 1
            glVertex2f(round(x1), y1)
        glEnd()

def drawPoint(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def drawLastTwoDigits():
    glPointSize(3)
    glBegin(GL_POINTS)

    midPoint(100, 300, 200, 300)

    DDA(100, 200, 100, 300)


    midPoint(100, 200, 200, 200)


    midPoint(200, 100, 200, 200)


    midPoint(100, 100, 200, 100)

    # ======================================================

    midPoint(350, 100, 350, 300)

    # lst = midPoint(250, 100, 350, 300)
    # i = 0
    # while i < len(lst):
    #     glVertex2f(lst[i][0], lst[i][1])
    #     i = i + 1

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
    glColor3f(1.0, 0.0, 3.0)
    drawLastTwoDigits()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"MIDpoint")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()