# -*- coding:utf-8 -*-
import csv

with open('test.csv', 'rb') as csvFile:
    reader = csv.reader(csvFile)
    for row in enumerate(reader,start=1):
        print row

    print('- - - - 我是分割线- - - - ')

    dictReader=csv.DictReader(csvFile)
    print dictReader
    for row in dictReader:
        print row