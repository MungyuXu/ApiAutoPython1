import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
    #????输出不了
    # a=open("d:\\workspace\\ApiAutoPython\\result.html",encoding="utf-8")
    # print(11)
    # a.read()
    # print(22)
    # soup=BeautifulSoup(a,"html.parser")
    # #prettify可以解析成html标准格式（有缩进）
    # print (soup.prettify()+"33")

    r=requests.get("http://www.cnblogs.com/yoyoketang/")
    blog=r.content
    soup=BeautifulSoup(blog,"html.parser")
    # print(type(soup))
    tag=soup.title
    p=soup.div
    # print(type(tag))
    #attrs打印出所有属性，字典格式
    print(p.attrs)
    #获取字典中的id属性
    print(p.attrs["id"])
    print(p.string)#none?
    # print(p)
    string=tag.string
    # print(type(string))
    # comment=soup.b.string #comment对象？
    # print(type(comment))