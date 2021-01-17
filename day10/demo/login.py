'''
    数据库版的登陆系统：（要求使用DBUtils数据库工具来进行操作）
        1.使用用户名和密码进行登陆
        数据库：goods
        表：t_admin
'''
from demo.DBUtils import DBUtils
db = DBUtils(database="goods")
sql = "select * from t_admin  where adminname = %s and adminpwd = %s"
while True:
    username = input("输入用户名：")
    password = input("输入密码：")
    param = [username,password]
    one = db.select(sql,param,mode="one")# one="()"  None
    if one != None:
        print("登陆成功！")
        break
    else:
        print("用户名或密码错误！请重新输入！")

db.releaseConnection()