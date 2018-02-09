from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

html=urlopen('http://www.pythonscraping.com/pages/page3.html')
bsobje=BeautifulSoup(html,'html.parser')
reg=re.compile(r'\.\.\/img\/gifts\/img.*\.jpg')
images=bsobje.findAll('img',{'src':reg})
for image in images:
    print(image['src'])