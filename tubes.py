from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from tmp import*

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

def MainProgram():
	print("Selamat datang pada program simulasi transformasi linier")
	print("Terdapat dua menu pada program ini yaitu simulasi 2 dimensi dan 3 dimensi")
	print("1. Untuk Memilih 2 dimensi, silakan input 2")
	print("2. Untuk Memilih 3 dimensi, silakan input 3")
	print("Masukan pilihan : ", end = "")
	x = int(input())
	if (x == 2):
		run2()
	else:
		run3()
	return

def run2():
	print("Masukan banyak titik: ", end="")
	n = int(input())
	print("Masukan titik-titik tersebut:")
	for i in range(0, n):
		x,y = map(int,input().split())
		tmp = Point(x+250,y+250)
		titik.arrPoint.append(tmp)
	init()

def translate(self, x, y):
	for i in self.arrPoint:
		i.x += x
		i.y += y 
	return self

def dilate(self, k):
	for i in self.arrPoint:
		i.x = ((i.x-250)*k + 250)
		i.y = ((i.y-250)*k + 250)
	for i in self.arrPoint:
		print(i.x, i.y)
	return self

def refresh2d(width, height):
  glViewport(0, 0, width, height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
  glMatrixMode (GL_MODELVIEW)
  glLoadIdentity()

def draw():
	while (True):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
		glLoadIdentity()
		refresh2d(width, height)
		glBegin(GL_LINES)
		glVertex2f(0, 250)
		glVertex2f(500, 250)

		glVertex2f(250,0)
		glVertex2f(250,500)

		glEnd()
		drawPolygon(titik)
		glutSwapBuffers()
		comm = input()
		if (comm == "translate"):
			x,y = map(int,input().split())
			P = translate(titik, x, y)
		elif (comm == "dilate"):
			x = input()
			P = dilate(titik, int(x))
			

def drawPolygon(x):
	#DrawAxis()
	glBegin(GL_POLYGON)
	for i in x.arrPoint:
		glVertex2f(i.x, i.y)
	glEnd()

def init():
	glutInit()                                             # initialize glut
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(501, 501)                      # set window size
	glutInitWindowPosition(0, 0)                           # set window position
	window = glutCreateWindow("Tubes Algeo")              # create window with title
	glutDisplayFunc(draw)                                  # set draw function callback
	glutIdleFunc(draw)                                     # draw all the time
	glutMainLoop()

def run3():
	return

MainProgram()
