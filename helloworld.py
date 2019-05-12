class helloworld(object):
	x = 0
	y = 0
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "Hello, world! : x = %d y = %d \n\n" % (self.x, self.y)


bop = helloworld(6, 9)
for i in range(0, 10):
	print(bop)
