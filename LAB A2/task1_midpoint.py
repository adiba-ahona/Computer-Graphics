from OpenGL.GL import *
from OpenGL.GLUT import *

def midPoint(x1, y1,x2, y2):
 # Setup initial conditions
    points = []
    if x1 == x2:
        for i in range(y1, y2):
            z = (x1, i)
            points.append(z)
        return points
    if y1 == y2:
        for i in range(x1, x2):
            z = (i, y1)
            points.append(z)
        return points

    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials of newly swapped
    dx = x2 - x1
    dy = y2 - y1

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

def drawid():
    glPointSize(3)
    glBegin(GL_POINTS)

    lst = midPoint(100, 300, 200, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1

    lst1 = midPoint(100, 200, 100, 300)
    i = 0
    while i < len(lst1):
        glVertex2f(lst1[i][0], lst1[i][1])
        i = i + 1

    lst = midPoint(100, 200, 200, 200)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1

    lst = midPoint(200, 100, 200, 200)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1

    lst = midPoint(100, 100, 200, 100)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1
# ======================================================
    lst = midPoint(250, 300, 350, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1

    lst = midPoint(350, 100, 350, 300)
    i = 0
    while i < len(lst):
        glVertex2f(lst[i][0], lst[i][1])
        i = i + 1

    # lst = midPoint(250, 100, 350, 300)------> [curved 7]
    # i = 0
    # while i < len(lst):
    #     glVertex2f(lst[i][0], lst[i][1])
    #     i = i + 1

    glEnd()


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)
    drawid()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(900, 800)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ID: 19101257 ; drawing 57")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
