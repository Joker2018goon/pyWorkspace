# -*- coding:utf-8 -*-
from urllib import urlopen
import urllib

'''
urlretrieve(url, filename=None, reporthook=None, data=None)
参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，filename 表示保存到本地的路径，header 表示服务器的响应头。
'''


def cbk(a, b, c):
    '''
    回调函数
    :param a:已经下载的数据块
    :param b:数据块大小
    :param c:远程文件大小
    :return:
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

url = 'https://www.baidu.com/'
local = 'D://baidu.html'
urllib.urlretrieve(url, local, cbk)
