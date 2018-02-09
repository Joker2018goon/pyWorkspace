from urllib2 import urlopen
import json

response=urlopen('http://freegeoip.net/json/50.78.253.58').read()
resJson=json.loads(response)
print(resJson['city'])
print(resJson)