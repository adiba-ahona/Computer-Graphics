
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_point(x,y):
   glPointSize(2) #pixel size
   glEnable(GL_POINT_SMOOTH)
   glBegin(GL_POINTS)
   glVertex2f(x,y)
   glEnd()

def midpointcircle(xc,yc,r):
   d = 1-r;
   x = 0;
   y = r;
   circlep(x, y, xc, yc);

   while (x<y):
       if d<0:
           d = d+2*x+3;
           x = x+1;
           #choose E
       else:
           d = d+2*x-2*y+5;
           x = x+1;
           y = y-1;

       circlep(x, y, xc, yc)

def circlep(x, y, xc, yc):
   zonechange(x, y, xc, yc)

def zonechange(x, y, xc, yc):

   new_x = x + xc
   new_y = y + yc
   draw_point(new_x, new_y)

   new_x = y + xc
   new_y = x + yc
   draw_point(new_x, new_y)

   new_x = -1 * y + xc
   new_y = x + yc
   draw_point(new_x, new_y)

   new_x = -1 *x + xc
   new_y = y + yc
   draw_point(new_x, new_y)

   new_x = -1 * x + xc
   new_y = -1 * y + yc
   draw_point(new_x, new_y)

   new_x = -1 * y + xc
   new_y = -1 * x + yc
   draw_point(new_x, new_y)

   new_x = y + xc
   new_y = -1 * x + yc
   draw_point(new_x, new_y)

   new_x = x+ xc
   new_y = -1 * y + yc
   draw_point(new_x, new_y)

def draw_circle():
   glColor3f(44.0/255.0, 203.0/255.0, 105.0/255.0)
   midpointcircle(400, 300, 200)

   glColor3f(103.0 / 255.0, 244.0 / 255.0, 246.0 / 255.0)
   midpointcircle(300, 300, 100)
   midpointcircle(500, 300, 100)
   midpointcircle(400, 400, 100)
   midpointcircle(400, 200, 100)

   glColor3f(246.0 / 255.0, 152.0 / 255.0, 142.0 / 255.0)
   midpointcircle(475, 366, 100)
   midpointcircle(325, 366, 100)
   midpointcircle(325, 233, 100)
   midpointcircle(475, 233, 100)

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
   iterate()
   # glColor3f(178.0, 242.0, 136.0) #konokichur color set (RGB)
   #call the draw methods here
   draw_circle()
   glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Midpoint Circle") #window name
glutDisplayFunc(showScreen)

glutMainLoop()