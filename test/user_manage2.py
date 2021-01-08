print('管理员登录'.center(50,'*'))
inuser = input('UserName:')
inpasswd = input('Password:')

#所有会员用户名
users = ['root','westos']
#所有会员密码
passwds = ['123','456']

if inuser == 'admin' and inpasswd == 'admin':
    print('管理员登录成功！')
    print('会员管理'.center(50,'*'))
    while True:
        print("""
            操作目录
    1.  添加会员信息
    2.  删除会员信息
    3.  查看会员信息
    4.  退出
    """)
        choice = input('请选择你的操作:')
        if choice == '1':
            print('添加会员信息'.center(50,'*'))
            AddUser = input('添加会员名:')
            if AddUser in users:
                print('用户%s已经存在' %(AddUser))
            else:
                AddPasswd = input('密码:')
                users.append(AddUser)
                passwds.append(AddPasswd)
                print('添加用户%s成功!' %AddUser)
        elif choice == '2':
            print('删除会员信息'.center(50,'*'))
            DelUser = input('删除会员名:')
            DelIndex = users.index(DelUser)
            users.remove(DelUser)
            passwds.pop(DelIndex)
            print('删除会员%s成功!' %DelUser)
        elif choice == '3':
            print('查看会员信息'.center(50,'*'))
            print('\t用户名\t密码')
            UserCount = len(users)
            for i in range(UserCount):
                print('\t%s\t%s' %(users[i],passwds[i]))
        elif choice == '4':
            exit()
        else:
            print('请输入正确的选择')
else:
    print('管理员登录失败!')