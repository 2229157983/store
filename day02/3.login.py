i=0
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    i=i+1
    if username != "jason" or password !="admin":
        print("用户名或密码错误！请重新输入！")
        if i == 3:
            print("三次用户名或密码输入错误，锁定！")
            break
    else:
        print("登录成功！")
        break