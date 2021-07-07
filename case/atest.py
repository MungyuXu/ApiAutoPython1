import  requests

print('123')
# par={"Keywords":"yoyoketang"}
# r=requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
r=requests.get('https://www.baidu.com')
print(r.status_code)
# print( r.text) #获取返回内容，不解码
print(r.encoding)  #编码
print(r.content)# 获取返回内容，解码,自动解码 gzip 和 deflate 压缩
print(r.headers)
print(r.cookies)
print(r.url)
print(r.raise_for_status())
