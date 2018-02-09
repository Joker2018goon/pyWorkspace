import urlparse
import csv

inurl='http://www.pythonscraping.com/pages/page3.html'
inurl=urlparse.urlparse(inurl).scheme+'://'+urlparse.urlparse(inurl).netloc
print(inurl)