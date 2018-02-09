# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen

html=urlopen('http://www.pythonscraping.com/pages/page1.html')
bsobj=BeautifulSoup(html.read())
print(bsobj)
print('--------------------')
print(bsobj.h1)
print('--------------------')
print(bsobj.title)