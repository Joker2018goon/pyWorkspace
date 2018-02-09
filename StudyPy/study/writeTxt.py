# -*- coding:utf-8 -*-
import os
with open("C:/Users/yanchunwei/Desktop/test.txt", "a+") as document:
    # document = open("C:/Users/yanchunwei/Desktop/test.txt", "w+")
    print "文件名: ", document.name
    document.write("\n这是我在文件末尾追加的内容！")
    print document.tell()
    # 输出当前指针位置
    document.seek(os.SEEK_SET)
    # 设置指针回到文件最初
    context = document.read()
    print context