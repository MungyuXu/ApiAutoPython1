import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.cnblogs.com/yoyoketang/")
blog=r.content
#用html.parser解析html
soup=BeautifulSoup(blog,"html.parser")
#获取所有class属性为dayTitle，返回tag类
times=soup.find_all(class_="dayTitle")
for i in times:
    a=i
    print(i.a.string)
