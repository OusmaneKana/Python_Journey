import urllib2
some_url="www.google.com"
content = urllib2.urlopen(some_url).read()
print content
