# coding=utf-8 
import xlrd
data = xlrd.open_workbook('returnlabel.xls')
table = data.sheets()[0] #通过索引顺序获取
nrows = table.nrows #行数
ncols = table.ncols #列数

      
for i in range(nrows):
    mc=table.row_values(i)[1].strip()
    lb=table.row_values(i)[2].strip()
    content="{'mc':'"+mc+"','type':'"+lb+"'},"+"\n"
    with open("test.txt","a",encoding='utf-8') as f:# 自带文件关闭功能，不需要再写f.close()
        f.write(content)    
    print(i,'条插入完成')


# mc=table.row_values(817)[1].strip()
# with open("test.txt","a",encoding='utf-8') as f:
#     f.write(mc) 
# print(mc)