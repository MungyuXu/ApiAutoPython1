# coding:utf-8
from bs4 import BeautifulSoup

import requests
import os
r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
fengjing = r.content
soup = BeautifulSoup(fengjing, "html.parser")
# 找出所有的标签
images = soup.find_all(class_="lazy")
# print images # 返回 list 对象
for i in images:
    jpg_rl = i["data-original"] # 获取 url 地址
    title = i["title"] # 返回 title 名称
    print(title)
    print (jpg_rl)
    print(os.getcwd())#获得当前脚本路径