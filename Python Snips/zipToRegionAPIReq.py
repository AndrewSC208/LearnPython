from urllib2 import Request, urlopen, URLError

zip = 92101

request = Request('http://api.zippopotam.us/us/%d', zip)

try:
  response = urlopen(request)
  data = response.read()
  print data
except URLError, e:
    print 'Got an error code:', e