import math

def translate(self, x, y):
	for i in self.arrPoint:
		i.x += x
		i.y += y
	return self

def dilate(self, k):
	for i in self.arrPoint:
		i.x = i.x*k
		i.y = i.y*k
	return self

def reflect(self, x, y):
	for i in self.arrPoint:
		tmp = i.x - x
		i.x = i.x - 2*tmp
		tmp = i.y - y
		i.y = i.y - 2*tmp
	return self

def shear(self, a, k):
	if (a=='x'):
		for i in self.arrPoint:
			i.x += i.y*k
	elif (a=='y'):
		for i in self.arrPoint:
			i.y += i.x*k
	return self

def rotate(self, deg, a, b):
	deg = (2*deg*math.acos(-1))/360.0
	for i in self.arrPoint:
		i.x -= a
		i.y -= b
		tmpx = i.x * math.cos(deg) - i.y * math.sin(deg)
		tmpy = i.x * math.sin(deg) + i.y * math.cos(deg)
		i.x = tmpx
		i.y = tmpy
	return self

def stretch(self, param, k):
	if (param == 'x'):
		for i in self.arrPoint:
			i.x *= k
	else:
		for i in self.arrPoint:
			i.y *= k
	return self

def custom (self, a, b, c, d):
	for i in self.arrPoint:
		tx = i.x * a + i.y * b
		ty = i.x * c + i.y * d
		i.x = tx
		i.y = ty
	return self

def reset():
	return