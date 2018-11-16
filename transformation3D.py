def translate3D(self, x, y, z):
	for i in self.arrPoint:
		i.x += x
		i.y += y
		i.z += z
	return self

def dilate3D(self, k):
	for i in self.arrPoint:
		i.x *= k
		i.y *= k
		i.z *= k
	return self
	
def reflect3D(self, x, y, z):
	for i in self.arrPoint:
		tmp = i.x - x
		i.x -= 2*tmp
		tmp = i.y - y
		i.y -= 2*tmp
		tmp = i.z - z
		i.z -= 2*tmp
	return self
	
def stretch3D(self, param, k):
	if (param == 'x'):
		for i in self.arrPoint:
			i.x = ((i.x-250)*k * 250)
	elif (param == 'y'):
		for i in self.arrPoint:
			i.y = ((i.y-250)*k * 250)
		else:
			for i in self.arrPoint:
				i.z = ((i.z-250)*k * 250)
	return self
	
def custom3D (self, a, b, c, d, e, f, g, h, i):
	for i in self.arrPoint:
		t.x = (i.x - 250) * a + (i.y - 250) * d + (i.z - 250) * g
		t.y = (i.x - 250) * b + (i.y - 250) * e + (i.z - 250) * h
		t.z = (i.x - 250) * c + (i.y - 250) * f + (i.z - 250) * i
		i.x = t.x + 250
		i.y = t.y + 250
		i.z = t.z + 250
	return self