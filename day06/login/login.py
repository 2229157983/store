#缓存器
database={}   #"jason":"root"

#将names.txt 文件的个人信息 放入database里
f=open("names.txt","r+",encoding="utf-8")
names=f.readlines()  #读取所有行数据
for item in names:#item:"jason,admin" 从每一行中遍历数据
    its=item.split(",")   # ["jason","admin"] 通过，切割数据，将用户名和密码分开
    database[its[0]]=its[1].replace("\n","")  #replace替换，将原来的数据替换成新数据

while True:
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    if username in database and password==database[username]:
        print("登陆成功")
        break
    else:
        print("登陆失败，用户名或密码错误！")