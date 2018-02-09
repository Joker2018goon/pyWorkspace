from urllib2 import urlopen,HTTPError,URLError
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsobj = BeautifulSoup(html, 'html.parser')
nalist = bsobj.findAll('span', {'class': 'green'})
for name in nalist:
    print(name.text)