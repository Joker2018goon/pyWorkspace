from urllib2 import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bsobj=BeautifulSoup(html.read(),'html.parser')
for child in bsobj.find('table',{'id':'giftList'}).tr.next_siblings:
    print(child)