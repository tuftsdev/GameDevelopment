# From http://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python/
class FooType:
	def __init__(self, id):
		self.id = id
		print self.id, 'born'

	def __del__(self):
		print self.id, 'died'

def make_foo():
	print 'Making...'
	ft = FooType(1)
	print 'Returning...'
	return ft

print "Calling..."
ft = make_foo()
print "End..."
