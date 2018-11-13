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
