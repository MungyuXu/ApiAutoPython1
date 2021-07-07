import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.cnblogs.com/yoyoketang/")
blog=r.content
#用html.parser解析html
soup=BeautifulSoup(blog,"html.parser")
# #获取所有class属性为dayTitle，返回tag类
times=soup.find_all(class_="dayTitle")
for i in times:
    a=i
    # 获取a标签文本,获取当前 Tag 的标签为 a 的 string 值?
    print(i.a.string)

#获取摘要父类 <divclass="c_b_p_desc">下多了一个子类 a,先获取 div 这个 Tag 类，tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出.因为摘要可以看成是第一个子元素，取下标[0]就可以读出来
# descs=soup.find_all(class_="postCon")
# for i in descs:
#     #tag的.contents属性可以将tag的子节点以列表的方式输出
#     c=i.div.contents[0]
#     print(c)
