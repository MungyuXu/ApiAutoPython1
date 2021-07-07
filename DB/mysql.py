import pymysql.cursors
#连接mysql数据库
connection=pymysql.connect(host='',
                           port=3306,
                           user='',
                           passwd='4',
                           db='scrm',
                           charset='utf8mb4')
try:
    #通过cursor创建游标
    cursor=connection.cursor()
    #创建sql语句并执行
    sql="SELECT * FROM scrm.scrm_mkt_activity limit 5"
    cursor.execute(sql)
    #获取所有记录列表
    results=cursor.fetchall()
    print(results)
    for data in results:
        print(data)
except Exception:print("查询失败")
#关闭游标链接
cursor.close()
#关闭数据库连接
connection.close()