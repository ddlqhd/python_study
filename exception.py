
import urllib2

req = urllib2.Request('http://bbs.csdn.net/asl')

try:
    response = urllib2.urlopen(req)
    print response.read()

except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code

    elif hasattr(e, 'reason'):
        print 'We failed to reach the server.'
        print 'Reason: ', e.reason

else:
    pass
