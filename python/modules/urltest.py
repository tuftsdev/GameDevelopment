import urllib2

page = urllib2.urlopen("http://www.cs.tufts.edu/~mchow").readlines()
print page
