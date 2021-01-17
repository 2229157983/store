import pymysql
con=pymysql.connect(host="localhost",user="root",password="",database="student")
cursor=con.cursor()#获取游标
sql="insert into student values('S12','小霞','女',22,3)"

result=cursor.execute(sql)#execute 执行sql语句并得到返回的结果
print(result)#打印最终结果

con.commit()#提交数据

cursor.close()#关闭游标
con.close()#关闭连接