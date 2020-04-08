# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# Created by Administrator on 2017/12/15
import json
import time
import requests
import os
import sys

in_ip = ['40.0.0.212','40.0.0.61']
user = 'wangxiang'
sig = 'd5efe95a172b11eab65b02b5f5d7d2c4' # 注:sig为数据库uic表中用户对应的sig
domain = 'http://127.0.0.1:8080'
api_token = '{"name":"' + user + '", "sig":"' + sig + '"}'
directiry = '/api/v1/graph/endpoint?q=[{0},{1}]'.format(in_ip[0],in_ip[1])

falcon_header = {
            "Apitoken": api_token,
            "X-Forwarded-For": "127.0.0.1",
            "Content-Type": "application/json",
            "name": user,
            "sig": sig
        }

params = {
    "url": domain + directiry,
    "headers": falcon_header,
    "timeout": 30
}
res1 = requests.get(**params)
data1 = json.loads(res1.text)
print(data1) 


directiry2="/api/v1/graph/endpoint_counter?eid=1"
params2 = {
    'url': domain + directiry2,
    'headers': falcon_header,
    'timeout': 30
}
res2 = requests.get(**params2)
data2 = json.loads(res2.text)
#print(data2)
