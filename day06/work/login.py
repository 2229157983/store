database = {}

welcome = '''
*****************************************
*                                       *
*****************************************
*   1.注册                              *
*   2.登录                              *
*   3.修改密码                           *
*   4.退出系统                           *
*****************************************
'''
def readnames():
    file = open("names.txt", "r+", encoding="utf-8")
    names = file.readlines()
    for item in names:
        its = item.split(",")
        database[its[0]] = {
            "username":its[0],
            "password":its[1],
            "sex":its[2],
            "age":its[3],
            "address":its[4],
            "path":its[5]
        }
    file.close()

def upData(username,password,sex,age,address,path):
    readnames()
    if username in database:
        print("用户已存在！")
    else:
        database[username] = {
            "username":username,
            "password":password,
            "sex":sex,
            "age":age,
            "address":address,
            "path":path
        }
        write = open("names.txt", "a+", encoding="utf-8")
        write.write("\r")
        for i in database[username]:
            write.write(database[username][i])
            if i == "path":
                write.write("")
            else:
                write.write(",")
        write.close()


def upPhoto(path):
    photo = open(path, "rb+")
    write = open("E:/photo/photo.jpg", "wb")
    data = photo.read()
    write.write(data)
    write.close()
    photo.close()
    print("上传成功！")

def addUser():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    sex = input("请输入性别：")
    age = input("请输入年龄：")
    address = input("请输入地址：")
    print("上传头像：")
    path1 = input("请输入头像路径：")
    last = ".jpg"
    path = path1 + last
    if path1 != path:
        path1 = path
    upData(username, password, sex, age, address, path1)
    upPhoto(path1)

def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username in database:
        if password == database[username]["password"]:
            print("登录成功！")
        else:
            print("账号或密码错误！")
    else:
        print("账号不存在！")

def chengePassword():
    username = input("请输入用户名：")
    password = input("请输入原密码：")
    if username in database:
        if password == database[username]["password"]:
            password1 = input("请输入新密码：")
            database[username]["password"] = password1
            write = open("names.txt", "w+", encoding="utf-8")
            for i in database:
                for j in database[i]:
                    write.write(database[i][j])
                    if j == "path":
                        write.write("")
                    else:
                        write.write(",")
            print("修改成功！")
        else:
            print("账号或密码错误！")
    else:
        print("账号不存在！")

while True:
    print(welcome)
    chose = input("请输入您的选项：")
    if chose == "1":
        addUser()
    elif chose == "2":
        login()
    elif chose == "3":
        chengePassword()
    elif chose == "4":
        print("恭喜发财！不送！")
        break
    else:
        print("您输入的选项不存在！")