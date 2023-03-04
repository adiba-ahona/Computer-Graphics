from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_point(x1,y1,x2,y2):
   glPointSize(4) #pixel size
   glEnable(GL_POINT_SMOOTH)
   glBegin(GL_POINTS)
   glVertex4f(x1,y1,x2,y2)
   glEnd()

INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

# Defining x_max, y_max and x_min, y_min for rectangle
# Since diagonal points are enough to define a rectangle
x_max = 300.0
y_max = 290.0
x_min = 100.0
y_min = 120.0


# Function to compute region code for a point(x, y)
def computeoc(x, y):
    oc = INSIDE
    if x < x_min: # to the left of rectangle
        oc |= LEFT
    elif x > x_max: # to the right of rectangle
        oc |= RIGHT
    if y < y_min:  # below the rectangle
        oc |= BOTTOM
    elif y > y_max:  # above the rectangle
        oc |= TOP

    return oc


# Implementing Cohen-Sutherland algorithm
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
def cohenSutherlandClip(x1, y1, x2, y2):
    draw_point(x1,y1,x2,y2)
    # Compute region codes for P1, P2
    oc1 = computeoc(x1, y1)
    oc2 = computeoc(x2, y2)
    accept = False

    while True:

        # If both endpoints lie within rectangle
        if oc1 == 0 and oc2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle
        elif (oc1 & oc2) != 0:
            break

        # Some segment lies within the rectangle
        else:
            x = 1.0
            y = 1.0
        if oc1 != 0:
            oc_out = oc1
        else:
            oc_out = oc2

        if oc_out & TOP:

            # point is above the clip rectangle
            x = x1 + (x2 - x1) * \
                (y_max - y1) / (y2 - y1)
            y = y_max

        elif oc_out & BOTTOM:

            # point is below the clip rectangle
            x = x1 + (x2 - x1) * \
                (y_min - y1) / (y2 - y1)
            y = y_min

        elif oc_out & RIGHT:

            # point is to the right of the clip rectangle
            y = y1 + (y2 - y1) * \
                (x_max - x1) / (x2 - x1)
            x = x_max

        elif oc_out & LEFT:

            # point is to the left of the clip rectangle
            y = y1 + (y2 - y1) * \
                (x_min - x1) / (x2 - x1)
            x = x_min

        # Now intersection point x, y is found
        # We replace point outside clipping rectangle
        # by intersection point
        if oc_out == oc1:
            x1 = x
            y1 = y
            oc1 = computeoc(x1, y1)

        else:
            x2 = x
            y2 = y
            oc2 = computeoc(x2, y2)


def iterate():
   glViewport(0, 0, 800, 800)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
   glMatrixMode (GL_MODELVIEW)
   glLoadIdentity()
def showScreen():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glLoadIdentity()
   #glFlush()
   iterate()
   glColor3f(178.0, 242.0, 136.0) #konokichur color set (RGB)
   #call the draw methods here
   cohenSutherlandClip(50, 140, 280, 310)
   draw_point(100,120,300,290)
   glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"19101257: LAB 4") #window name
glutDisplayFunc(showScreen)

glutMainLoop()