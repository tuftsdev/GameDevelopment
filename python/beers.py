beers = 99

while beers > 1:
	print str(beers) + " bottles of beer on the wall, " + str(beers) + " bottles of beer"
	beers = beers - 1
	if beers >= 2:
		print "Take one down and pass it around, " + str(beers) + " bottles of beer on the wall\n"
	else:
		print "Take one down and pass it around, " + str(beers) + " bottle of beer on the wall\n"
print "1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n" # Print an extra return
print "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
