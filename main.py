from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transformation2D import *
from transformation3D import *
from random import *
import sys
import math

width = 1000
height = 1000

class Point:
	arrPoint = []
	def __init__(self, x, y):
		self.x = x
		self.y = y

titik = Point(0,0)
initial = Point(0,0)

#Draw Shape of the Blocks (So every changes be made, call this method)
def drawShape(x):
    # glBegin(GL_POLYGON)
    # for i in x.arrPoint:
	   # glVertex2f(i.x,i.y)
    # glEnd()
    glBegin(GL_POLYGON)
    for i in x.arrPoint:
        glColor3f(random(), random(), random())
        glVertex2f(i.x, i.y)
    glEnd()

#Draw Axis
def drawAxis():
    glBegin(GL_LINES)
    glVertex2f(0,width)
    glVertex2f(0, -width)

    glVertex2f(height,0)
    glVertex2f(-height,0)

    glEnd()


#Draw all the parts for the window
def draw():
    initial = titik
    while (True):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
        glLoadIdentity()
        refresh2d(width, height)
        drawAxis()
        drawShape(titik)
        glutSwapBuffers()
        comm = input()
        if (comm == "exit"):
            sys.exit()
        #elif (comm == "reset"):

        elif (comm != "multiple"):
            doCommand2D(comm)
        elif (comm == "multiple"):
            tmp = input()
            n = int(tmp)
            for i in range(0, n):
                comm = input()
                doCommand2D(comm)

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

#Make the window of the program
def makeWindow():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Tubes Algeo")              # create window with title
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()

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
        tmp = Point(float(x),float(y))
        titik.arrPoint.append(tmp)
    makeWindow()

#3D was selected (calling all transformation and method for 3D)
def run3d():
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
