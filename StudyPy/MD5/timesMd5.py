# -*- coding:utf-8 -*-
import hashlib


def times_Md5(data,n):
    result=data
    m=hashlib.md5()
    for i in range(0,n):
        m.update(result)
        result=m.hexdigest()
    return result

print times_Md5('加密',1)