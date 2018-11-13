import math

def translate(self, x, y):
	for i in self.arrPoint:
		i.x += x
		i.y += y
	return self

def dilate(self, k):
	for i in self.arrPoint:
		i.x = ((i.x-250)*k + 250)
		i.y = ((i.y-250)*k + 250)
	return self

def reflect(self, x, y):
	for i in self.arrPoint:
		tmp = i.x - (250 + x)
		i.x = i.x - 2*tmp
		tmp = i.y - (250 + y)
		i.y = i.y - 2*tmp
	return self

def shear(self, a, k):
	if (a=='x'):
		for i in self.arrPoint:
			i.x += ((i.y-250)*k)
	elif (a=='y'):
		for i in self.arrPoint:
			i.y += ((i.x-250)*k)
	return self

def rotate(self, deg, a, b):
	deg = (2*deg*math.acos(-1))/360.0
	for i in self.arrPoint:
		i.x -= 250
		i.x -= a
		i.y -= 250
		i.y -= b
		tmpx = i.x * math.cos(deg) - i.y * math.sin(deg)
		tmpy = i.x * math.sin(deg) + i.y * math.cos(deg)
		i.x = tmpx + 250
		i.y = tmpy + 250
	return self

def stretch(self, param, k):
	if (param == 'x'):
		for i in self.arrPoint:
			i.x -= 250
			i.x *= k
			i.x += 250
	else:
		for i in self.arrPoint:
			i.y -= 250
			i.y *= k
			i.y += 250
	return self

def custom (self, a, b, c, d):
	for i in self.arrPoint:
		i.x -= 250
		i.y -= 250
		t.x = i.x * a + i.y * b
		t.y = i.x * c + i.y * d
		i.x = t.x + 250
		i.y = t.y + 250
	return self

def reset():
	return