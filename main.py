from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transformation2D import *
from transformation3D import *
from random import *
import sys
import math

Wireframe = True
width = 700
height = 700
tra_x = 0
tra_y = 0
tra_z = 0
x_rot = 0
y_rot = 0

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.arrPoint = []

    def add_point(self, x, y, z):
        temp = Point(float(x), float(y), float(z))
        self.arrPoint.append(temp)

initial = Point(0,0,0)
titik = Point(0,0,0)

#Draw Shape of the Blocks (So every changes be made, call this method)
def drawShape2D(x):
    glBegin(GL_POLYGON)
    for i in x.arrPoint:
        glColor3f(random(), random(), random())
        glVertex2f(i.x, i.y)
    glEnd()

#Draw Axis
def drawAxis():
    glBegin(GL_LINES)

    glColor3f(random(), random(), random())
    glVertex2f(0,width)
    glVertex2f(0, -width)

    glColor3f(random(), random(), random())
    glVertex2f(height,0)
    glVertex2f(-height,0)

    glEnd()

#Draw all the parts for the window
def draw2D():
    while (True):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
        glLoadIdentity()
        refresh2d(width, height)
        drawAxis()
        drawShape2D(titik)
        glutSwapBuffers()
        comm = input()
        if (comm == "exit"):
            sys.exit()
        elif (comm != "multiple"):
            doCommand2D(comm)
        elif (comm == "multiple"):
            tmp = input()
            n = int(tmp)
            for i in range(0, n):
                comm = input()
                doCommand2D(comm)

def draw3D():
    while (True):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()

        gluLookAt(
        0.0, 0.0, 3.0,
        0.0, 0.0, 0.0,
        0.0, 1.0, 0.0)

        glTranslatef(0.0, 0.0, -5.0)

        glRotatef(x_rot, 1.0, 0.0, 0.0)
        glRotatef(y_rot, 0.0, 1.0, 0.0)
        glTranslatef(tra_x, tra_y, tra_z)

        drawShape3D(titik)
        glFlush()
        glutSwapBuffers()

        comm = input()
        if (comm == "dilate"):
            n = input()
            P = dilate3D(titik, float(n))
        elif (comm == "exit"):
            sys.exit()

def drawShape3D(x):
    glBegin(GL_QUADS)
    
    glColor3f(1.0, 0.0,  0.0)
    
    #front
    glVertex3f(x.arrPoint[0].x, x.arrPoint[0].y, x.arrPoint[0].z)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(x.arrPoint[1].x, x.arrPoint[1].y, x.arrPoint[1].z)
    glVertex3f(x.arrPoint[2].x, x.arrPoint[2].y, x.arrPoint[2].z)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(x.arrPoint[3].x, x.arrPoint[3].y, x.arrPoint[3].z)
    
    #back
    glVertex3f(x.arrPoint[4].x, x.arrPoint[4].y, x.arrPoint[4].z)
    glVertex3f(x.arrPoint[5].x, x.arrPoint[5].y, x.arrPoint[5].z)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(x.arrPoint[6].x, x.arrPoint[6].y, x.arrPoint[6].z)
    glVertex3f(x.arrPoint[7].x, x.arrPoint[7].y, x.arrPoint[7].z)

    glColor3f(0.0, 1.0, 0.0)
    
    #left
    glVertex3f(x.arrPoint[8].x, x.arrPoint[8].y, x.arrPoint[8].z)
    glVertex3f(x.arrPoint[9].x, x.arrPoint[9].y, x.arrPoint[9].z)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(x.arrPoint[10].x, x.arrPoint[10].y, x.arrPoint[10].z)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(x.arrPoint[11].x, x.arrPoint[11].y, x.arrPoint[11].z)

    #right
    glVertex3f(x.arrPoint[12].x, x.arrPoint[12].y, x.arrPoint[12].z)
    glVertex3f(x.arrPoint[13].x, x.arrPoint[13].y, x.arrPoint[13].z)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(x.arrPoint[14].x, x.arrPoint[14].y, x.arrPoint[14].z)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(x.arrPoint[15].x, x.arrPoint[15].y, x.arrPoint[15].z)

    glColor3f(0.0, 0.0, 1.0)

    #top
    glVertex3f(x.arrPoint[16].x, x.arrPoint[16].y, x.arrPoint[16].z)
    glVertex3f(x.arrPoint[17].x, x.arrPoint[17].y, x.arrPoint[17].z)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(x.arrPoint[18].x, x.arrPoint[18].y, x.arrPoint[18].z)
    glVertex3f(x.arrPoint[19].x, x.arrPoint[19].y, x.arrPoint[19].z)
    glColor3f(1.0, 0.0, 0.0)

    #bottom
    glVertex3f(x.arrPoint[20].x, x.arrPoint[20].y, x.arrPoint[20].z)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(x.arrPoint[21].x, x.arrPoint[21].y, x.arrPoint[21].z)
    glVertex3f(x.arrPoint[22].x, x.arrPoint[22].y, x.arrPoint[22].z)
    glVertex3f(x.arrPoint[23].x, x.arrPoint[23].y, x.arrPoint[23].z)

    glEnd()

#do the command for 2d only
def doCommand2D(comm):
    if (comm == "translate"):
        x, y = input().split()
        P = translate(titik, float(x), float(y))
    elif (comm == "dilate"):
        x = input()
        P = dilate(titik, float(x))
    elif (comm == "reflect"):
        x, y = input().split()
        P = reflect(titik, float(x), float(y))
    elif (comm == "shear"):
        a, k = input().split()
        P = shear(titik, a, float(k))
    elif (comm == "rotate"):
        deg, a, b = input().split()
        P = rotate(titik, float(deg), float(a), float(b))
    elif (comm == "stretch"):
        param, x = input().split()
        P = stretch(titik, param, float(x))
    elif (comm == "custom"):
        a,b,c,d = input().split()
        P = custom(titik, float(a), float(b), float(c), float(d))
    elif (comm == "reset"):
        P = reset(titik, initial)


def keyPressed(*args):
    global tra_x
    global tra_y
    global tra_z
    global x_rot
    global y_rot
    if (args[0] == b"w"):
        tra_z -= 0.1
    elif (args[0] == b"s"):
        tra_z += 0.1
    elif (args[0] == b"a"):
        tra_x += 0.1
    elif (args[0] == b"d"):
        tra_x -= 0.1
    elif (args[0] == b"u"):
        x_rot += 2.0
        y_rot += 2.0 
    elif (args[0] == b"y"):
        x_rot -= 2.0
        y_rot -= 2.0
    elif (args[0] == b"x"):
        global Wireframe
        if Wireframe==False:
            glPolygonMode(GL_FRONT, GL_LINE)    
            glPolygonMode(GL_BACK, GL_LINE)
            Wireframe=True
        elif Wireframe ==True:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)
            Wireframe=False
    # print(args[0])
    # glutPostRedisplay()

#Make the window of the program
def makeWindow2D():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Tubes Algeo 2D")              # create window with title
    glutDisplayFunc(draw2D)                                  # set draw function callback
    glutIdleFunc(draw2D)                                     # draw all the time
    glutMainLoop()

def makeWindow3D():
    global window
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Tubes Algeo 3D")
    glutDisplayFunc(draw3D)
    glutIdleFunc(draw3D)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(width, height)
    glutMainLoop()

def InitGL(Width, Height):                
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                   
    glDepthFunc(GL_LESS)                
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT, GL_LINE)    
    glPolygonMode(GL_BACK, GL_LINE)     
    glShadeModel(GL_SMOOTH)                

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    
                                        
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                       
        Height = 1
    glViewport(0, 0, Width, Height)        
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

#Buffer the drawing
def refresh2d(width, height):
    glViewport(0,0 , width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-width, width, -height, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

#2D was selected (calling all transformation and method for 2D)
def run2d():
    print("Masukan banyak titik: ")
    n = int(input())
    print("Masukan titik-titik tersebut:")
    for i in range(0, n):
        x,y = input().split()
        titik.add_point(x,y,0)
        initial.add_point(x,y,0)
    makeWindow2D()

#3D was selected (calling all transformation and method for 3D)
def run3d():
    tmpArr = [(-0.5, -0.5, 0.5), 
    (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), 
    (-0.5, -0.5, -0.5),(-0.5, 0.5, -0.5), ( 0.5, 0.5, -0.5),( 0.5, -0.5, -0.5), (-0.5, -0.5, 0.5)
    ,(-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), ( 0.5, -0.5, -0.5), ( 0.5, 0.5, -0.5), 
    ( 0.5, 0.5, 0.5), ( 0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), ( 0.5, 0.5, 0.5), ( 0.5, 0.5, -0.5), 
    (-0.5, 0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5),( 0.5, -0.5, -0.5),( 0.5, -0.5, 0.5)]
    for i in tmpArr:
        titik.add_point(i[0], i[1], i[2])
        initial.add_point(i[0], i[1], i[2])
    makeWindow3D()
    return

#Main program (include making the windows)
print("Selamat datang pada program simulasi transformasi linier")
print("Terdapat dua menu pada program ini yaitu simulasi 2 dimensi dan 3 dimensi")
print("1. Untuk Memilih 2 dimensi, silakan input 2")
print("2. Untuk Memilih 3 dimensi, silakan input 3")
print("Masukan pilihan : ")
x = int(input())
if (x == 2):
    run2d()
else:
    run3d()
