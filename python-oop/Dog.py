class Dog:
	""" Dog dog dog! """
	def __init__(self):
		""" Initializer """
		print "A dog is born..."
		self.name = "Fido"

	def setName (self, n):
		self.name = n
            
	def bark(self):
		print self.name + " says Arf!"

if __name__ == "__main__":
	brian = Dog()
	brian.setName("Brian")
	for i in range(5):
		brian.bark()

	lily = Dog()
	lily.setName("Lily")
	lily.bark()

	stu = Dog()
	stu.bark()
	