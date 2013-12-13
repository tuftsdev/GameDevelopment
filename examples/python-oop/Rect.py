class Rect:
	''' A class that describes a rectangle '''

	def __init__(self, someWidth, someHeight, someLabel, someColor):
		print "In __init__ or constructor for new instance " + someLabel
		self.width = someWidth
		self.height = someHeight
		self.label = someLabel
		self.color = someColor

	def perimeter(self):
		print 2 * (self.width + self.height)
		
	def area(self):
		print (self.width * self.height)
		
if __name__ == "__main__":
	x = Rect(10, 10, "Simple", (255, 255, 255))
	x.perimeter()
	x.area()
	
else:
	print "Go away"
