from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from transformation2D import *
from transformation3D import *
import sys

width = 500
height = 500

class Point:
	arrPoint = []
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def writePoint(self):
		print(self.x, self.y)

titik = Point(0,0)

#Draw Shape of the Blocks (So every changes be made, call this method)
def drawShape(x):
    glBegin(GL_POLYGON)
    for i in x.arrPoint:
		glVertex2f(i.x, i.y)
    glEnd()

#Draw Axis
def drawAxis():
    glBegin(GL_LINES)
    glVertex2f(0, 250)
    glVertex2f(500, 250)

    glVertex2f(250,0)
    glVertex2f(250,500)

    glEnd()


#Draw all the parts for the window
def draw():
    while (True):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
        glLoadIdentity()
        refresh2d(width, height)
        drawAxis()
        drawShape(titik)
        glutSwapBuffers()
        comm = raw_input()
        if (comm == "translate"):
            x, y = raw_input().split()
            P = translate(titik, int(x), int(y))
        elif (comm == "dilate"):
			x = input()
			P = dilate(titik, int(x))
        elif (comm == "reflect"):
            x, y = raw_input().split()
            P = reflect(titik, int(x), int(y))
        elif (comm == "shear"):
            a, k = raw_input().split()
            P = shear(titik, a, int(k))
        elif (comm == "exit"):
            sys.exit()

#Make the window of the program
def makeWindow():
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(500, 500)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Tubes Algeo")              # create window with title
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()

#Buffer the drawing
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

#2D was selected (calling all transformation and method for 2D)
def run2d():
    print("Masukan banyak titik: ")
    n = int(input())
    print("Masukan titik-titik tersebut:")
    for i in range(0, n):
        x,y = raw_input().split()
        tmp = Point(int(x)+250,int(y)+250)
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
