# -*- coding:utf-8 -*-
import requests

# 调用百度接口
r=requests.get('https://www.baidu.com')

# r.status_code Http请求返回的状态（响应码） 200 - - 表示连接成功 ，404 - -表示失败
print(u'接口响应码：',r.status_code)
print('======================================================')

# r.text HTTP 响应内容的字符串形式，即，URL对应的页面内容
print('页面内容：',r.text)
print('======================================================')

# r.encoding 从HTTP header中猜测的响应内容编码形式
print('编码形式:',r.encoding)
# r.apparent_encoding 从内容中分析响应内容编码形式（备选编码形式）
print(r.apparent_encoding)
print('======================================================')

# r.content HTTP响应内容的二进制形式
print('HTTP响应内容的二进制形式:',r.content)