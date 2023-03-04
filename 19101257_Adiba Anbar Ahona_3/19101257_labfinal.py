from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_point(x,y):
   glPointSize(4) #pixel size
   glEnable(GL_POINT_SMOOTH)
   glBegin(GL_POINTS)
   glVertex2f(x,y)
   glEnd()

def midpointcircle(xc,yc,r):
   d = 1-r
   x = 0
   y = r
   circlep(x, y, xc, yc)

   while (x<y):
       if d<0:
           d = d+2*x+3
           x = x+1
           #choose E
       else:
           d = d+2*x-2*y+5
           x = x+1
           y = y-1

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

def find_zones(dx, dy):
  if abs(dx) > abs(dy):
      if dx>0 and dy>=0:
          return 0
      elif dx<=0 and dy>=0:
          return 3
      elif dx>=0 and dy>=0:
          return 7
      elif dx<=0 and dy<=0:
          return 4
  else:
      if dx>=0 and dy>=0:
          return 1
      elif dx <= 0 and dy >= 0:
          return 2
      elif dx<=0 and dy<=0:
          return 5
      elif dx>=0 and dy<=0:
          return 6

def convert_to_zone0(x1, y1, x2, y2, zone):
  if zone == 0:
    return x1, y1, x2, y2
  elif zone == 1:
    return y1, x1, y2, x2
  elif zone == 2:
    return y1, -x1, y2, -x2
  elif zone == 3:
    return -x1, y1, -x2, y2
  elif zone == 4:
    return -x1, -y1, -x2, -y2
  elif zone == 5:
    return -y1, -x1, -y2, -x2
  elif zone == 6:
    return -y1, x1, -y2, x2
  elif zone == 7:
    return x1, -y1, x2, -y2
  return x1,y1,x2,y2


def convert_original_zone(x, y, zone):
  if zone == 0:
    return x, y
  if zone == 1:
    return y, x
  if zone == 2:
    return -y, x
  if zone == 3:
    return -x, y
  if zone == 4:
    return -x, -y
  if zone == 5:
    return -y, -x
  if zone == 6:
    return y, -x
  if zone == 7:
    return x, -y


def mid_point_count(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone_no = find_zones(dx, dy)
    x1, y1, x2, y2 = convert_to_zone0(x1, y1, x2, y2, zone_no)
    d0 = 2 * dy - dx
    dNE = 2 * (dy - dx)
    dE = 2 * dy
    x = x1
    y = y1

    while x < x2:
        p = x
        q = y
        p, q = convert_original_zone(x, y, zone_no)
        draw_point(p, q)
        x = x + 1

        if (d0 < 0):
            d0 = d0 + dE
        else:
            d0 = d0 + dNE
            y = y + 1

def drawscenery():
    #river
    glColor3f(55.0 / 255.0,62.0 / 255.0, 5.0 / 255.0)
    mid_point_count(10, 150, 1000, 350)
    mid_point_count(8, 140, 998, 340)
    #tree:
    glColor3f(30.0 / 255.0, 100.0 / 255.0, 25.0 / 255.0)
    midpointcircle(75, 170, 20)
    midpointcircle(115, 150, 25)
    midpointcircle(50, 140, 25)
    midpointcircle(110, 200, 25)
    midpointcircle(60, 220, 30)
    midpointcircle(40, 180, 20)

    #tree
    glColor3f(95.0 / 255.0, 84.0 / 255.0, 64.0 / 255.0)
    mid_point_count(70, 150, 70, 50)
    mid_point_count(85, 150, 85, 50)

    #office1
    glColor3f(113.0 / 255.0, 129.0 / 255.0, 133.0 / 255.0)
    mid_point_count(180, 320, 280, 320) #top
    mid_point_count(180, 320, 180, 50)#left
    mid_point_count(180, 250, 280, 250)#middle
    mid_point_count(280, 320, 280, 50)#right
    mid_point_count(180, 150, 280, 150)#middle1
    mid_point_count(180, 50, 280, 50)#bottom
    mid_point_count(200, 100, 200, 50)
    mid_point_count(260, 100, 260, 50)
    mid_point_count(200, 100, 260, 100)

    #office2
    glColor3f(113.0 / 255.0, 129.0 / 255.0, 133.0 / 255.0)
    mid_point_count(680, 220, 780, 220) #top
    mid_point_count(680, 220, 780, 50)#left
    mid_point_count(680, 150, 780, 150)#middle
    mid_point_count(780, 220, 880, 50)#right
    mid_point_count(750, 120, 750, 50)#door
    mid_point_count(720, 120, 720, 50)#bottom
    mid_point_count(720, 120, 750, 120)
    #
    #tree
    glColor3f(95.0 / 255.0, 84.0 / 255.0, 64.0 / 255.0)
    mid_point_count(350, 150, 350, 50)
    mid_point_count(365, 150, 365, 50)

    glColor3f(35.0 / 255.0, 120.0 / 255.0, 35.0 / 255.0)
    midpointcircle(360, 180, 26)
    # midpointcircle(360, 220, 20)
    midpointcircle(360, 260, 20)
    midpointcircle(380, 200, 25)
    midpointcircle(340, 200, 25)
    midpointcircle(345, 230, 20)
    midpointcircle(375, 230,20)

    #bird
    glColor3f(139.0 / 255.0, 215.0 / 255.0, 203.0 / 255.0)
    mid_point_count(390, 500, 400, 510)
    mid_point_count(390, 500, 380, 510)

    mid_point_count(490, 520, 500, 530)
    mid_point_count(490, 520, 480, 520)

    #bridge
    glColor3f(53.0 / 255.0, 35.0 / 255.0, 126.0 / 255.0)
    mid_point_count(10, 350, 1200, 350)
    mid_point_count(10, 370, 1200, 370)

    glColor3f(139.0 / 255.0, 126.0 / 255.0, 210.0 / 255.0)
    mid_point_count(500, 350, 600, 450)
    mid_point_count(550, 370, 650, 470)#

    mid_point_count(700, 350, 600, 450)
    mid_point_count(750,370, 650, 470)#

    mid_point_count(300, 350, 400, 450)
    mid_point_count(350,370, 450, 470)

    mid_point_count(500, 350, 400, 450)
    mid_point_count(550, 370, 450, 470)

    mid_point_count(300, 350, 200, 450)
    mid_point_count(350, 370, 250, 470)

    mid_point_count(100, 350, 200, 450)
    mid_point_count(150, 370, 250, 470)

    mid_point_count(100, 450, 100, 350)
    mid_point_count(150, 470, 150, 370)

    mid_point_count(80, 450, 80, 350)
    mid_point_count(130, 470, 130, 370)
    #
    mid_point_count(60, 450, 60, 350)
    mid_point_count(110, 470, 110, 370)

    mid_point_count(100, 450, 150, 470)#openingroof
    mid_point_count(80, 450, 130, 470)
    mid_point_count(60, 450, 110, 470)

    #cloud
    glColor3f(62.0 / 255.0, 173.0 / 255.0, 229.0 / 255.0)
    midpointcircle(300, 550, 20)
    midpointcircle(320, 520, 20)
    midpointcircle(280, 520, 20)

    glColor3f(60.0 / 255.0, 170.0 / 255.0, 225.0 / 255.0)
    midpointcircle(600, 550, 20)
    midpointcircle(620, 520, 20)
    midpointcircle(580, 520, 20)

    #lightening
    glColor3f(221.0 / 255.0, 241.0 / 255.0, 70.0 / 255.0)
    mid_point_count(580, 490, 610, 510)
    mid_point_count(580, 490, 610, 495)
    mid_point_count(580, 470, 610, 495)

    #water
    glColor3f(28.0 / 255.0, 197.0 / 255.0, 251.0 / 255.0)
    mid_point_count(50, 300, 80, 300)
    mid_point_count(70, 320, 100, 320)
    mid_point_count(100, 250, 130, 250)
    mid_point_count(110, 290, 140, 290)
    mid_point_count(120, 270, 150, 270)
    mid_point_count(300, 270, 330, 270)
    mid_point_count(350, 300, 380, 300)
    mid_point_count(400, 290, 430, 290)
    mid_point_count(450, 320, 480, 320)
    mid_point_count(420, 250, 450, 250)
    mid_point_count(520, 270, 550, 270)
    mid_point_count(620, 310, 650, 310)
    mid_point_count(600, 320, 630, 320)
    glColor3f(30.0 / 255.0, 31.0 / 255.0, 153.0 / 255.0)
    mid_point_count(650, 340, 690, 340)
    mid_point_count(550, 340, 550, 340)
    mid_point_count(470, 308, 500, 308)
    mid_point_count(10,50, 900, 50)

    #car
    glColor3f(228.0 / 255.0, 3.0 / 255.0, 16.0 / 255.0)
    mid_point_count(450, 100, 500, 150)
    mid_point_count(500, 150, 600, 150)
    mid_point_count(650, 100, 600, 150)
    mid_point_count(650, 100, 650, 70)
    mid_point_count(410, 100, 450, 100)
    mid_point_count(410, 100, 410, 70)
    mid_point_count(410, 70, 650, 70)
    glColor3f(88.0 / 255.0, 75.0 / 255.0, 56.0 / 255.0)
    midpointcircle(500, 70, 20)
    midpointcircle(600, 70, 20)



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
   # glColor3f(178.0, 242.0, 136.0) #konokichur color set (RGB)
   #call the draw methods here
   drawscenery()
   glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"19101257: CSE423 Lab Final") #window name
glutDisplayFunc(showScreen)

glutMainLoop()