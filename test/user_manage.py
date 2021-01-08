'''
实现后台管理员管理前台会员信息系统，具体要求如下：
1. 后台管理员只有一个用户: admin, 密码: admin
2. 当管理员登陆成功后， 可以管理前台会员信息.
3. 会员信息管理包含:
      添加会员信息
      删除会员信息
      查看会员信息
      退出

'''
user = ["aaa","bbb"]
password = ["123","456"]

print("————————————————————欢迎登录后台管理界面——————————————————")
admuser = input("管理员用户名：")
admpass = input("管理员密码：")
if admuser == "admin" and admpass == "admin":
    print("登录成功！")
    print("****会员信息管理****")
    print("   1.添加会员信息  ")
    print("   2.删除会员信息  ")
    print("   3.查看会员信息  ")
    print("   4.退出  ")
    choice = input("请选择操作，输入序号1-4：")
    # 1-添加会员信息
    if choice == "1":
        adduser=input("输入新的会员用户名：")
        if adduser in user:
            print("用户名已存在！")
        else:
            user.append(adduser)
            addpass = input("输入新的会员密码：")
            password.append(addpass)
            print("添加会员信息成功！")
            print("目前系统中的会员用户名如下：")
            for i in user:
                print(i)
    #2-删除会员信息
    elif choice == '2':
        #遍历用户名
        print("目前系统中的会员用户名如下：")
        for i in user:
            print(i)
        deluser = input("请输入要删除的用户名：")
        num = user.index(deluser)
        #print("您要删除的用户名不存在！")
        print(num)
        user.pop(num)
        password.pop(num)
        print("删除成功！")
        print("目前系统中的会员用户名如下：")
        for i in user:
            print(i)
    # 3-查看会员信息
    elif choice == '3':
        # 遍历用户名
        print("目前系统中的会员用户名如下：")
        for i in user:
            print(i)
    # 4-退出
    elif choice == '4':
        print("退出系统！")
        exit()
    else: print("输入选项错误！")


else:
    print("用户名或密码错误！")