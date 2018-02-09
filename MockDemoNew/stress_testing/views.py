# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from mock_pro.models import *
from FUC import toolbox
from django.http import HttpResponse
from stress_testing import models
import datetime,copy,time,threading
import requests
import tool
import json,random

def index(req):
    return render(req,'stress_testing/index.html')
#返回一个页面
def single_interface(req):
    return render(req,'stress_testing/testing.html')
#单接口压测
def stress_testing(req):
    # type=0
    result_tmp={}
    try:
        #前端数据获取处理
        thread_count, cycles, delay, control_type, url, type, header, data, response_code, ramup_time, serialnum, name, serviceIp=tool.get_request_data(req)

        try:
            result=tool.thread_config(thread_count, cycles, delay, control_type, url, type, header, data, response_code,ramup_time,serialnum,name,serviceIp)
            result_tmp = tool.dict_to_json(result)

        except:
            print '请求失败'
    except:
        print '首次进入单接口压测页面'



    return HttpResponse(result_tmp)

