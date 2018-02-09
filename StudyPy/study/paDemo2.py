# -*- coding:utf-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import paDemo

# 收集网站上发现的所有外链列表
allExternalLinks=set()
allInternalLinks=set()
def getAllExternalLinks(urlSite):
    html=urlopen(urlSite)
    bsObj=BeautifulSoup(html,'html.parser')
    externalLinks= paDemo.getExternalLinks(bsObj, urlSite)
    internalLinks= paDemo.getInternalLinks(bsObj, urlSite)
    for link in externalLinks:
        if link not in allExternalLinks:
            allExternalLinks.add(link)
            print(link)

    for link in internalLinks:
        if link not in allInternalLinks:
            print('即将获取链接的URL是'+link)
            allInternalLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks('http://oreilly.com')