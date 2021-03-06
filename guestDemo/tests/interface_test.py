# -*- coding:utf-8 -*-
import requests
import unittest
import json

class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.result=''
        self.url='http://127.0.0.1:8000/api/get_event_list/'

    def tearDown(self):
        print(self.result)

    def test_get_event_null(self):
        # 发布会id为空
        r=requests.get(self.url,params={'eid':''})
        self.result=r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    def test_get_event_error(self):
        # 发布会id不存在
        r=requests.get(self.url,params={'eid':10})
        self.result = r.json()
        # print(self.result['status'])
        # print(type(self.result['status']))
        self.assertEqual(int(self.result['status']),10022)
        self.assertEqual(self.result['message'],'query result is empty')

    def test_get_event_success(self):
        # 发布id为1，查询成功
        r=requests.get(self.url,params={'eid':1})
        # r.encoding = 'utf-8'
        print(r.encoding)
        print(r.url)
        print(r.content)
        print('==========================================================================================')
        print(r.json())
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')
        self.assertEqual(self.result['data']['name'],'红米Pro发布会')

if __name__ == '__main__':
    unittest.main()