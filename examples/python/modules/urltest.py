import urllib2

page = urllib2.urlopen("http://www.reddit.com/").readlines()
print page
