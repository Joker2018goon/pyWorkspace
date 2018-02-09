# -*- coding:utf-8 -*-
import os
from urllib2 import urlopen
import urllib
from bs4 import BeautifulSoup

downloadDirectory = r'downloaded'
baseurl = r'http://pythonscraping.com'


def getAbsoluteURL(baseurl, source):
    if source.startswith(r'http://www.'):
        url = r'http://' + source[11:]
    elif source.startswith(r'http://'):
        url = source
    elif source.startswith(r'www.'):
        url = r'http://' + source[4:]
    else:
        url = baseurl + r'/' + source

    if baseurl not in url:
        return None
    return url


def getDownloadPath(baseurl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace(r'www', '')
    path = path.replace(baseurl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen(r'http://www.baidu.com')
bsObj = BeautifulSoup(html, 'html.parser')
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseurl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urllib.urlretrieve(fileUrl, getDownloadPath(baseurl, fileUrl, downloadDirectory))
