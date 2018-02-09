# -*- coding:utf-8 -*-
import csv
from urllib2 import urlopen
from bs4 import BeautifulSoup

with open('table.csv','wb') as csvFile:
    writer=csv.writer(csvFile)
    html=urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
    bsObj=BeautifulSoup(html,'html.parser')
    # 主对比表格是当前页面上的第一个表格
    table=bsObj.findAll('table',{'class':'wikitable'})[0]
    rows=table.findAll('tr')
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)