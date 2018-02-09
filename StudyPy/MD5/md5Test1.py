# -*- coding:utf-8 -*-
import hashlib
md5_obj=hashlib.md5()
text=r'test.py'
md5_obj.update(text)
print md5_obj.hexdigest()