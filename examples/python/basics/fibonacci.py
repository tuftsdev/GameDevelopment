def fibonacci (n):
	""" Returns the Fibonacci number for given integer n """
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)

n = 25
for i in range(n):
	result = fibonacci(i)
	print "The fibonacci number for ", i, " is ", result
