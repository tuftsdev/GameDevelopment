bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'Developer'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'Musician'}
charlie = dict(name='Charlie Weis', age=48, pay=1000000, job='Coach')
database = {}
database['bob'] = bob
database['sue'] = sue
database['charlie'] = charlie
if __name__ == '__main__':
	for entry in database:
		print entry, ' => ', database[entry]
