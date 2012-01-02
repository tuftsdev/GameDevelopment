class Foo:
	""" My first class """
	def __init__(self):
		print "Hi!"

	def setx (self, x):
		self.x = x
		
	def bar (self):
		print self.x

if __name__ == "__main__":
	f = Foo()
	f.setx(20)
	f.bar

# What is the output (and why)?
