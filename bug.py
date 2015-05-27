
import urllib2

req = urllib2.Request('http://bbs.csdn.net/asl')

try:
    response = urllib2.urlopen(req)
    print response.read()

except urllib2.URLError, e:
    print e.code
