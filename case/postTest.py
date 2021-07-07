import json
import re
import unittest

import requests

# help(requests) #查看相关注释内容和案例
# r=requests.post('https://t-luffy.gaodunwangxiao.com/api/v1/topic/page/1/disable')

#非json入参
# data={"yoyo":"helloworld","pythonQQ群":"226296743"}
# r=requests.post('http://httpbin.org/post',data=data)

#json入参

payload={"orderBy":"createdAt","pageIndex": 1,"pageSize": 10,"sort": 1,"where": {"newStaffId": 0,"oldStaffId": 0}}
# data_json=json.dumps(payload)  这个不要了
r=requests.post('https://t-luffy.gaodunwangxiao.com/api/v1/staff/departing/list',json=payload)
# print(r2.content)

# data={"yoyo":"helloworld","pythonQQ群":"226296743"}
# data_json=json.dumps(data)
# r=requests.post('http://httpbin.org/post',json=data_json)
# print(data_json)
# print(r.url)
# print(r.text)
# print(r.json())
#加（）表示正则表达式的开始和结束，可提取出参中的参数供后续步骤使用
kk=re.compile(r'"info":"(.*)"')
a=re.findall(kk,r.text)
print(a)
help(unittest)