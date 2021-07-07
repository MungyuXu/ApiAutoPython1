import xlrd as xlrd

data=xlrd.open_workbook("d:\\workspace\\ApiAutoPython\\test.xls")
table=data.sheet_by_name(u'Sheet1')#通过名称获取
table1=data.sheets()[0]#通过索引顺序获取
table2=data.sheet_by_index(0)#通过索引顺序获取
nrows=table.nrows#获取总行数
ncols=table.ncols#获取总列数
print(table2.row_values(0))#获取第一行值
print(table2.col_values(0))#获取第一列值
print(table.row_values(0)[1])